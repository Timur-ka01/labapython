import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from my_family import get_family_info

def test_father_height():
    assert get_family_info()['father_height'] == '177'

def test_total_height():
    assert get_family_info()['total_height'] == 522