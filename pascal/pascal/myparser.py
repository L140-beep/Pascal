from .lexer import Lexer
from .terminals import Token, TokenType, TokenExpect
from copy import deepcopy
class ParserException(Exception):
    ...

class Parser:  
    def __init__(self):
        self.tokens = []
        self.current_token: Token = None
        self.lexer = Lexer()
        self.prev_token: Token = None
        self.start = 0
    
    def factor(self):
        token = self.current_token
        
        if self.start == 0:
            if token.type == TokenType.BEGIN:
                self.start = 1
            else:
                raise ParserException("Invalid token")
        
        match token.type:
            case TokenType.NUMBER:
                self.tokens.append(token)
                self.check_type(TokenExpect.NUMBER)
            
            case TokenType.BEGIN:
                self.tokens.append(token)
                self.check_type(TokenExpect.BEGIN)
                
            case TokenType.END:
                self.tokens.append(token)
                self.check_type(TokenExpect.END)
                
            case TokenType.SUB_END:
                self.tokens.append(token)
                self.check_type(TokenExpect.SUB_END)
            
            case TokenType.VARIABLE:
                if self.IS_RVARIABLE(token):
                    token = Token(TokenType.R_VARIABLE, token.value)
                    self.tokens.append(token)
                    self.check_type(TokenExpect.R_VARIABLE)
                else:
                    token = Token(TokenType.L_VARIABLE, token.value)
                    self.tokens.append(token)
                    self.check_type(TokenExpect.L_VARIABLE)
                    
            case TokenType.END_INSTRUCTION:
                self.tokens.append(token)
                self.check_type(TokenExpect.END_INSTRUCTION)
            
            case TokenType.ASSIGNMENT:
                self.tokens.append(token)
                self.check_type(TokenExpect.ASSIGNMENT)
            
            case TokenType.L_VARIABLE:
                self.tokens.append(token)
                self.check_type(TokenExpect.L_VARIABLE)
            
            case TokenType.R_VARIABLE:
                self.tokens.append(token)
                self.check_type(TokenExpect.R_VARIABLE)
            
            case TokenType.RPAREN:
                self.tokens.append(token)
                self.check_type(TokenExpect.RPAREN)
                
            case TokenType.LPAREN:
                self.tokens.append(token)
                self.check_type(TokenExpect.LPAREN)            
            
            case TokenType.OPERATOR:
                self.tokens.append(token)
                self.check_type(TokenExpect.OPERATOR)  
            case _:
                raise ParserException("Invalid token")

            
    def check_type(self, expected : TokenExpect):
        self.prev_token = self.current_token
        self.current_token = self.lexer.next()
        
        token = self.current_token
        
        if self.prev_token is None and self.current_token.type != TokenType.BEGIN:
            ParserException("blablabla")
        
        if self.current_token is None:
            if expected == TokenExpect.END:
                return
            else:
                raise ParserException("Invalid argument")

        if token.type == TokenType.VARIABLE:
            if self.IS_RVARIABLE(token):
                self.current_token = Token(TokenType.R_VARIABLE, self.current_token.value)
            else:
                self.current_token = Token(TokenType.L_VARIABLE, self.current_token.value)
                
        if self.current_token.type in expected.value:
            self.factor()
        else:
            print(self.prev_token)
            raise ParserException(f"Unexpected token {self.current_token.type}, expected {expected.value}") 

    def IS_RVARIABLE(self, token):
        return self.prev_token.type in [TokenType.ASSIGNMENT, TokenType.OPERATOR]
        
    def init_parser(self, s: str):
        self.lexer.init_lexer(s)
        self.current_token = self.lexer.next()
        self.prev_token: Token = None
        self.tokens = []
        self.start = 0
    
    def get_tokens(self):
        return deepcopy(self.tokens)