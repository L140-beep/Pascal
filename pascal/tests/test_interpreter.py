import pytest
from pascal.interpreter import Interpreter


class TestInterpreter:
    def test_init(self):
        inter = Interpreter()
    
    def test_eval(self):
        inter = Interpreter()
        assert inter.eval("pascal/tests/1.pas") == [{}]
        assert inter.eval("pascal/tests/2.pas") == [{'x' : 17.0, 'y' : 11.0}]
        assert inter.eval("pascal/tests/3.pas") == [{"y" : 2.0, "x" : 11.0}, {"a" : 3.0, "b" : 18.0, "c" : -15.0}]
    
    