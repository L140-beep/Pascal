from .terminals import TerminalsType, TokenType, Token

class LexerException(Exception):
    ...

class Lexer:
    def __init__(self):
        self.pos = 0
        self.string = ""
        self.current_char = ""
    
    def init_lexer(self, string : str):
        if not string:
            raise LexerException("Empty string!")
        self.pos = 0
        self.string = string
        self.current_char = string[self.pos]
    
    
    def forward(self):
        self.pos += 1
        
        if len(self.string) == 1:
            self.current_char = ""
        else:        
            if self.pos == len(self.string):
                self.current_char = ""
            else:
                self.current_char = self.string[self.pos]
    
    def next(self):
        while self.current_char != "":
            if self.current_char.isspace():
                self.skip()
                continue
            
            if self.current_char in TerminalsType.NUMBER.value:
                return Token(TokenType.NUMBER, self.number())
            
            if self.current_char.isalpha():
                value = self.variable()
                
                if value in TokenType.BEGIN.value:
                    return Token(TokenType.BEGIN, value)
                
                else: 
                    char = self.current_char
                    self.forward()
                    if value + char in TokenType.END.value:
                        return Token(TokenType.END, value + char)
                    
                    elif value + char in TokenType.SUB_END.value:
                        return Token(TokenType.SUB_END, value + char)

                    else:
                        self.pos -= 1
                        self.current_char = self.string[self.pos]
                        return Token(TokenType.VARIABLE, value)
                    

            if self.current_char in TerminalsType.ASSIGNMENT.value:
                return Token(TokenType.ASSIGNMENT, self.assignment())
            
            if self.current_char in TerminalsType.OPERATOR.value:
                return Token(TokenType.OPERATOR, self.operator())
            
            if self.current_char in TerminalsType.LPAREN.value:
                char = self.current_char
                self.forward()
                return Token(TokenType.LPAREN, char)
            
            if self.current_char in TerminalsType.RPAREN.value:
                char = self.current_char
                self.forward()
                return Token(TokenType.RPAREN, char)
            
            if self.current_char in TerminalsType.END_INSTRUCTION.value:
                char = self.current_char
                self.forward()
                return Token(TokenType.END_INSTRUCTION, char)
            
            raise LexerException("Unexpected terminal")
    
    def operator(self) -> str:
        result = []
    
        while self.current_char != "" and self.current_char in TerminalsType.OPERATOR.value:
            result.append(self.current_char)
            self.forward()
        return "".join(result)


    def assignment(self) -> str:
        result = []
        while self.current_char != "" and self.current_char in TerminalsType.ASSIGNMENT.value:
            result.append(self.current_char)
            self.forward()
        
        # if not flag:
        #     self.forward()
        
        
        return "".join(result)
    
    
    def variable(self) -> str:
        result = []
        flag = 0
        while self.current_char != "" and self.current_char.isalpha():
            flag = 1
            result.append(self.current_char)
            self.forward()    
        
        if not flag:
            self.forward()
        
        return "".join(result)
    
    
    def prev(self):
        return self.string[self.pos - 1]
    
    def skip(self):
        while self.current_char != "" and self.current_char.isspace():
            self.forward()
    
    def number(self) -> str:
        result = []
        
        while self.current_char != "" and \
                (self.current_char in TerminalsType.NUMBER.value):
            result.append(self.current_char)
            self.forward()
        return "".join(result)