# interpreter.py
from .tree import NodeVisitor,Node, BinOp, Number, UnaryOp
from .parser import Parser
from .tokens import TokenType
import sys
sys.path.append("..")
class NumInterpreterException(Exception):
    ...

class NumInterpreter(NodeVisitor):

    def __init__(self):
        self.parser = Parser()

    def visit(self, node: Node) -> float:
        match node:
            case Number():
                return self.visit_number(node)
            case BinOp():
                return self.visit_binop(node)
            case UnaryOp():
                return self.visit_unary(node)
        raise NumInterpreterException("invalid node")

    def visit_number(self, node: Number) -> float:
        # print(f"Visit number {node}")
        return float(node.value.value)

    def visit_unary(self, node: Number) -> float:
        match node.op.type:
            case TokenType.PLUS:
                return + self.visit(node.node)
            case TokenType.MINUS:
                return - self.visit(node.node)
        raise NumInterpreterException("invalid unary op")

    def visit_binop(self, node: BinOp) -> float:
        match node.op.type:
            case TokenType.PLUS:
                return self.visit(node.left) + self.visit(node.right)
            case TokenType.MINUS:
                return self.visit(node.left) - self.visit(node.right)
            case TokenType.MUL:
                return self.visit(node.left) * self.visit(node.right)
            case TokenType.DIV:
                return self.visit(node.left) / self.visit(node.right)
        raise NumInterpreterException("invalid operator")

    def eval(self, s: str) -> float:
        self.parser.init_parser(s)
        tree = self.parser.expr()
        return self.visit(tree)
