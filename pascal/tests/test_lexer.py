import pytest
from pascal.lexer import Lexer
from pascal.terminals import Token, TokenType



class TestLexer:
    def test_init(self):
        lexer = Lexer()
        lexer.init_lexer("y := 12")
    
    def test_next(self):
        lexer = Lexer()
        
        lexer.init_lexer("y := 12 + 4")
        assert lexer.next() == Token(TokenType.VARIABLE, 'y')
        assert lexer.next() == Token(TokenType.ASSIGNMENT, ':=')
        assert lexer.next() == Token(TokenType.NUMBER, '12')
        assert lexer.next() == Token(TokenType.OPERATOR, '+')
        assert lexer.next() == Token(TokenType.NUMBER, '4')
    
        lexer.init_lexer("BEGIN END := 12 END; END.")
        assert lexer.next() == Token(TokenType.BEGIN, 'BEGIN')
        assert lexer.next() == Token(TokenType.VARIABLE, 'END')
        assert lexer.next() == Token(TokenType.ASSIGNMENT, ':=')
        assert lexer.next() == Token(TokenType.NUMBER, '12')
        assert lexer.next() == Token(TokenType.SUB_END, 'END;')
        assert lexer.next() == Token(TokenType.END, 'END.')
        
        
        lexer.init_lexer("BEGIN BEGIN y := 12; END; END.")
        assert lexer.next() == Token(TokenType.BEGIN, 'BEGIN')
        assert lexer.next() == Token(TokenType.BEGIN, 'BEGIN')
        assert lexer.next() == Token(TokenType.VARIABLE, 'y')
        assert lexer.next() == Token(TokenType.ASSIGNMENT, ':=')
        assert lexer.next() == Token(TokenType.NUMBER, '12')
        assert lexer.next() == Token(TokenType.END_INSTRUCTION, ';')
        assert lexer.next() == Token(TokenType.SUB_END, 'END;')
        assert lexer.next() == Token(TokenType.END, 'END.')
        
        lexer.init_lexer("BEGIN BEGIN y := ((12 + 12)); END; END.")
        assert lexer.next() == Token(TokenType.BEGIN, 'BEGIN')
        assert lexer.next() == Token(TokenType.BEGIN, 'BEGIN')
        assert lexer.next() == Token(TokenType.VARIABLE, 'y')
        assert lexer.next() == Token(TokenType.ASSIGNMENT, ':=')
        assert lexer.next() == Token(TokenType.LPAREN, '(')
        assert lexer.next() == Token(TokenType.LPAREN, '(')
        assert lexer.next() == Token(TokenType.NUMBER, '12')
        assert lexer.next() == Token(TokenType.OPERATOR, '+')
        assert lexer.next() == Token(TokenType.NUMBER, '12')
        assert lexer.next() == Token(TokenType.RPAREN, ')')
        assert lexer.next() == Token(TokenType.RPAREN, ')')
        assert lexer.next() == Token(TokenType.END_INSTRUCTION, ';')
        assert lexer.next() == Token(TokenType.SUB_END, 'END;')
        assert lexer.next() == Token(TokenType.END, 'END.')