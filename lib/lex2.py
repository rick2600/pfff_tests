import ply.lex as lex

from graphviz import Digraph

# https://github.com/dabeaz/ply
# https://www.dabeaz.com/ply/ply.html

class PFFFLexer(object):    
    # List of token names. This is always required
    tokens = (
        'LPAREN',
        'RPAREN',
        'LBRACKET',
        'RBRACKET',
        'COMMA',
        'NODE_PARENT',
        'NODE',
        'LITERAL',
        'ID',
        'SEMICOLON',
        'LCURLY',
        'RCURLY'
    )

    # Regular expression rules for simple tokens
    #t_NODE_PARENT       = r'[A-Z][a-zA-Z0-9_]*\('
    t_NODE              = r'[A-Z][a-zA-Z0-9_]*'
    t_LPAREN            = r'\('
    t_RPAREN            = r'\)'
    t_LBRACKET          = r'\['
    t_RBRACKET          = r'\]'
    t_LCURLY            = r'{'
    t_RCURLY            = r'}'
    t_COMMA             = r'\,'
    t_LITERAL           = r'"[^"]*"'
    t_ID                = r'i_\d+'
    t_SEMICOLON         = r';'

    # A regular expression rule with some action code
    # Note addition of self parameter since we're in a class
    def t_NODE_PARENT(self, t):
        r'[A-Z][a-zA-Z0-9_]*\('
        t.value = t.value[0:-1] 
        return t

    # Define a rule so we can track line numbers
    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def set_data(self, data):
        self.data = data
        self.parse()

    def parse(self):
        self.lexer.input(self.data)
    
    def get_token(self):
        return self.lexer.token()
    
    # Test it output
    def test(self):
        print self.data
        print "="*80
        level = 0 
        for tok in iter(self.lexer.token, None):
            pad = " " * level
            if tok.value == '(': level += 4
            if tok.value == ')': level -= 4
            print "%s%s => %s " % (pad, repr(tok.type).ljust(12), repr(tok.value))

