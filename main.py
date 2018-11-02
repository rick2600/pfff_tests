from lib.lex2 import *
from lib.ast import *

def main():
    data = ''
    filename = 'ex3.ast'
    with open("examples/%s" % filename, "r") as f:
        data = f.read()

    # Lex
    lexer = PFFFLexer()
    lexer.build()
    lexer.set_data(data)
    #lexer.test()
    
    # Build AST
    ast = ASTBuilder().build_lex2(lexer)

    # Debug AST
    ast_printer = ASTPrinter(ast)
    ast_printer.save_and_show(filename)



if __name__ == "__main__":
    main()