from .tokens import Token, TokenType

class LexerException(Exception):
    ...

class Lexer:

    def __init__(self):
        self.pos = 0
        self.text = ""
        self.current_char = ""

    def init_lexer(self, text: str):
        self.pos = 0
        self.text = text
        self.current_char = self.text[self.pos]

    def forward(self):
        self.pos += 1
        if self.pos == len(self.text):
            self.current_char = ""
        else:
            self.current_char = self.text[self.pos]

    def next(self) -> Token:
        while self.current_char != "":
            if self.current_char.isspace():
                self.skip()
                continue
            if self.current_char.isdigit():
                return Token(TokenType.NUMBER, self.number())
            if self.current_char == "+":
                ch = self.current_char
                self.forward()
                return Token(TokenType.PLUS, ch)
            if self.current_char == "-":
                ch = self.current_char
                self.forward()
                return Token(TokenType.MINUS, ch)
            if self.current_char == "*":
                ch = self.current_char
                self.forward()
                return Token(TokenType.MUL, ch)
            if self.current_char == "/":
                ch = self.current_char
                self.forward()
                return Token(TokenType.DIV, ch)
            if self.current_char == "(":
                ch = self.current_char
                self.forward()
                return Token(TokenType.LPAREN, ch)
            if self.current_char == ")":
                ch = self.current_char
                self.forward()
                return Token(TokenType.RPAREN, ch)
            raise LexerException("bad token")
        return Token(TokenType.EOL, "")

    def skip(self):
        while self.current_char != "" and self.current_char.isspace():
            self.forward()

    def number(self) -> str:
        result = []
        while self.current_char != "" and \
                (self.current_char.isdigit() or 
                self.current_char == '.'):
            result.append(self.current_char)
            self.forward()
        return "".join(result)