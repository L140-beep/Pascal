from .lexer import Lexer
from .myparser import Parser
from .terminals import TokenType
from .ilib.interpreter import NumInterpreter

from copy import deepcopy

class InterpreterException(Exception):
    ...

class Interpreter:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.variables = []
        self.current_level = -1
        self.numinterpreter = NumInterpreter()
    
    def restart(self):
        self.variables = []
        self.current_level = -1
    
    def eval(self, filepath):
        file = open(filepath)
        data = file.read()
        self.parser.init_parser(data)
        self.parser.factor()
        file.close()
        
        tokens = self.parser.get_tokens()

        for i in range(len(tokens)):
            match tokens[i].type:
                case TokenType.BEGIN:
                    self.current_level += 1
                    self.variables.append({})
                case TokenType.SUB_END:
                    self.current_level -= 1
                case TokenType.END:
                    print("Complete!")
                    break
                case TokenType.L_VARIABLE:
                    prev_i = i
                    i, self.variables[self.current_level][tokens[prev_i].value] = self.makeStatement(i, tokens)
        
        variables = deepcopy(self.variables)
        
        self.restart()
        return variables
    
    def findVariable(self, id):
        for i in range(0, self.current_level):
            keys = self.variables[i].keys()
            
            if id in keys:
                return self.variables[i][id]
            
        return False
    
    def makeStatement(self, index, tokens):
        statement = ""
        for i in range(index, len(tokens)):
            match tokens[i].type:
                case TokenType.ASSIGNMENT:
                    pass
                case TokenType.NUMBER | TokenType.OPERATOR | TokenType.LPAREN | TokenType.RPAREN:
                    statement += tokens[i].value
                case TokenType.R_VARIABLE:
                    try:
                        statement += str(int(self.variables[self.current_level][tokens[i].value]))
                    except KeyError:
                        value = self.findVariable(tokens[i].value)
                        if value:
                            statement += str(int(value))
                        else:
                            raise InterpreterException(f"Undefined variable {tokens[i].value}")
                case TokenType.END_INSTRUCTION:
                    result = self.numinterpreter.eval(statement)
                    return i, result
                
        raise InterpreterException("EXPECTED END_INSTRUCTION")