from pascal.pascal.terminals import TokenType, Token
from pascal.pascal.lexer import Lexer
from pascal.pascal.myparser import Parser
from pascal.pascal.interpreter import Interpreter


inter = Interpreter()
print(inter.eval("pascal/tests/3.pas") )
# parser = Parser()
# parser.init_parser('y := 12;')
# parser.factor()

# lexer = Lexer()

# lexer.init_lexer("y := 12;")

# print(lexer.next())
# print(lexer.next())
# print(lexer.next())
# print(lexer.next())
# print(lexer.next())
# print(lexer.next())
