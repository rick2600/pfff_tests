from lib.lex2 import *
from lib.ast import *
from lib.ast_analyzer import *
import sys
import os


def get_ast(filepath):
    data = ''
    with open(filepath, "r") as f:
        data = f.read()

    # Lex
    lexer = PFFFLexer()
    lexer.build()
    lexer.set_data(data)
    #lexer.test()

    # Build AST
    ast = ASTBuilder().build_lex2(lexer)
    return ast
       

def main():
    if len(sys.argv) < 2:
        print "Usage: %s <pfff_file.ast>" % (sys.argv[0])
        sys.exit(0)


    filepath = os.path.abspath(sys.argv[1])
    filename = os.path.basename(filepath)
    temp_img = os.path.join('/tmp', filename + ".png")

    ast = get_ast(filepath)
    # Debug AST
    ast_printer = ASTPrinter(ast)
    ast_printer.save_and_show(filename)

    #ast_analyzer = ASTAnalyzer(ast)
    #assigns = ast_analyzer.find_all('Assign')

    #for a in assigns:
    #    print ast_analyzer.get_assign_target(a)


if __name__ == "__main__":
    main()