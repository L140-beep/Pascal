# Tokens.py
from enum import Enum, auto

class TokenType(Enum):
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    DIV = auto()
    MUL = auto()
    EOL = auto()
    LPAREN = auto()
    RPAREN = auto()


class Token:

    def __init__(self, type_:TokenType, value: str):
        self.type = type_
        self.value = value

    def __str__(self) -> str:
        return f"Token ({self.type}, {self.value})"
