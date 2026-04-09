import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zoo import manage_zoo

def test_bear_added():
    assert 'bear' in manage_zoo()['zoo']

def test_elephant_removed():
    assert 'elephant' not in manage_zoo()['zoo']