import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shopping import get_best_prices

def test_returns_dict():
    assert isinstance(get_best_prices(), dict)

def test_has_pech():
    assert 'печенье' in get_best_prices()