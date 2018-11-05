from graphviz import Digraph


class Node(object):
    def __init__(self, token, node_id):
        self.parent = None
        self.node_id = node_id
        self.type = token.type[:]
        self.value = token.value[:]
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


class ASTBuilder(object):
    def __init__(self):
        self.node_id = 0

    def create_node(self, token):
        node = Node(token, self.node_id)
        self.node_id += 1
        return node        

    def build(self, lexer):
        root = None
        while True:
            tok = lexer.get_token()            
            if not tok: 
                break
            
            print tok.value
        return root


    def build_lex2(self, lexer):
        root = None
        parents = []
        node = None
        last_node = None

        while True:
            tok = lexer.get_token()            
            if not tok: 
                break

            t = tok.type

            if t in ['LBRACKET', 'RBRACKET', 'ID', 'SEMICOLON']: continue

            if t == 'NODE_PARENT':
                node = self.create_node(tok)
                if root == None:
                    root = node

                if len(parents) > 0:
                    parents[-1].add_child(node)

                parents.append(node)

            elif t == 'NODE' or t == 'LITERAL':
                node = self.create_node(tok)
                node.parent = parents[-1]
                node.parent.add_child(node)
            elif t == 'LPAREN':
                parents.append(parents[-1])
            elif t == 'RPAREN':
                parents.pop()
                

        return root



class ASTPrinter(object):
    def __init__(self, root):
        self.root = root

    def save_and_show(self, filename):
        g = Digraph('G', filename=filename, format='png')
        self.build_graph(self.root, g)
        g.view()

    def build_graph(self, node, g):
        for child in node.children:
            label1 = "%d %s" % (node.node_id, node.value)
            label2 = "%d %s" % (child.node_id, child.value)
            g.node(label1)
            
            if len(child.children) == 0:
                g.node(label2, shape='box', style='filled', fillcolor='lightblue2')
            
            g.edge(label1, label2)
            self.build_graph(child, g)        
