from enum import Enum, auto


class TerminalsType(Enum):
    NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ASSIGNMENT = [':', '=']
    OPERATOR = ['+', '-', '/', '*']
    END_INSTRUCTION = [';']
    LPAREN = ['(']
    RPAREN = [')']
    # NUMBER_SEPARATOR = ['.']
    # CONDITION_SEPARATOR = [',']

class TokenType(Enum):
    BEGIN = ["BEGIN"]
    END = ["END."]
    SUB_END = ["END;"]
    VARIABLE = auto()
    L_VARIABLE = auto()
    R_VARIABLE = auto()
    OPERATOR = auto()
    ASSIGNMENT = auto()
    NUMBER = auto()
    END_INSTRUCTION = auto()
    LPAREN = auto()
    RPAREN = auto()
    
class TokenExpect(Enum):
    END_INSTRUCTION = [TokenType.BEGIN, TokenType.END, TokenType.L_VARIABLE, TokenType.SUB_END]
    BEGIN = [TokenType.L_VARIABLE, TokenType.END, TokenType.SUB_END]
    END = [None]
    SUB_END = [TokenType.BEGIN, TokenType.END, TokenType.L_VARIABLE]
    
    ASSIGNMENT = [TokenType.NUMBER, TokenType.R_VARIABLE]
    L_VARIABLE = [TokenType.ASSIGNMENT]
    
    R_VARIABLE = [TokenType.OPERATOR, TokenType.END_INSTRUCTION, TokenType.RPAREN]
    NUMBER = [TokenType.END_INSTRUCTION, TokenType.OPERATOR, TokenType.RPAREN]
    OPERATOR = [TokenType.NUMBER, TokenType.R_VARIABLE, TokenType.LPAREN]
    LPAREN = [TokenType.NUMBER, TokenType.R_VARIABLE, TokenType.LPAREN]
    RPAREN = [TokenType.OPERATOR, TokenType.END_INSTRUCTION, TokenType.RPAREN]
    
    
class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value
    
    def __str__(self) -> str:
        return f"Token ({self.type}, {self.value})"
    
    def __eq__(self, right : "Token"):
        return self.type == right.type and self.value == right.value