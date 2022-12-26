import pytest
from pascal.myparser import Parser, ParserException
from pascal.terminals import Token, TokenType
class TestParser:
    def test_init(self):
        parser = Parser()
        parser.init_parser('y')
        parser.init_parser('y := 12;')
    
    def test_factor(self):
        parser = Parser()
        parser.init_parser('BEGIN y := 12; END.')
        parser.factor()
        assert parser.get_tokens() == [Token(TokenType.BEGIN, 'BEGIN'), 
                                     Token(TokenType.L_VARIABLE, 'y'), Token(TokenType.ASSIGNMENT, ':='), Token(TokenType.NUMBER, '12'), Token(TokenType.END_INSTRUCTION, ';'),
                                     Token(TokenType.END, 'END.')]
        
        
        with pytest.raises(ParserException):
            parser.init_parser('y := 12;')
            parser.factor()
        
        with pytest.raises(ParserException):
            parser.init_parser('BEGIN y  a := 12; END.')
            parser.factor()
        
        with pytest.raises(ParserException):
            parser.init_parser('BEGIN y 12; END.')
            parser.factor()
        
        with pytest.raises(ParserException):
            parser.init_parser('BEGIN y 12; END;')
            parser.factor()

        with pytest.raises(ParserException):
            parser.init_parser('BEGIN y  a := 12;')
            parser.factor()