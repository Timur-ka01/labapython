import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from garden import analyze_flowers

def test_common_flowers():
    assert 'ромашка' in analyze_flowers()['common']

def test_only_garden():
    assert 'роза' in analyze_flowers()['only_garden']