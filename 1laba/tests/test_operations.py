import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operations import calculate_expression

def test_returns_25():
    assert calculate_expression() == 25

def test_returns_int():
    assert isinstance(calculate_expression(), int)