# interpreter.py
from .tokens import Token, TokenType
from .lexer import Lexer
from .tree import Node, BinOp, Number, UnaryOp

class ParserException(Exception):
    ...

class Parser:

    def __init__(self):
        self.current_token: Token = None
        self.lexer = Lexer()

    def check_type(self, type_:TokenType):
        if self.current_token.type == type_:
            self.current_token = self.lexer.next()
            return
        raise ParserException(f"Invalid token order. Expected {type_}, Received {self.current_token}")

    def factor(self) -> Node:
        token = self.current_token
        match token.type:
            case TokenType.PLUS:
                self.check_type(TokenType.PLUS)
                return UnaryOp(token, self.factor())
            case TokenType.MINUS:
                self.check_type(TokenType.MINUS)
                return UnaryOp(token, self.factor())
            case TokenType.NUMBER:
                self.check_type(TokenType.NUMBER)
                return Number(token)
            case TokenType.LPAREN:
                self.check_type(TokenType.LPAREN)
                result = self.expr()
                self.check_type(TokenType.RPAREN)
                return result
        raise ParserException("invalid factor")

    def term(self) -> Node:
        ops = [TokenType.DIV, TokenType.MUL]
        result = self.factor()
        while self.current_token.type in ops:
            token = self.current_token
            match token.type:
                case TokenType.DIV:
                    self.check_type(TokenType.DIV)
                    # result /= self.factor()
                case TokenType.MUL:
                    self.check_type(TokenType.MUL)
                    # result *= self.factor()
            result = BinOp(result, token, self.factor())
        return result

    def expr(self) -> Node:
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self.term()
        while self.current_token.type in ops:
            token = self.current_token
            match token.type:
                case TokenType.PLUS:
                    self.check_type(TokenType.PLUS)
                case TokenType.MINUS:
                    self.check_type(TokenType.MINUS)
            result = BinOp(result, token, self.term())
        return result

    def init_parser(self, s: str):
        self.lexer.init_lexer(s)
        self.current_token = self.lexer.next()
