# tests/test_distance.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from distance import get_distances

def test_returns_dict():
    assert isinstance(get_distances(), dict)

def test_moscow_london():
    assert round(get_distances()['Moscow']['London'], 2) == 148.66