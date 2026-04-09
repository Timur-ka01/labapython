import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from circle import calculate_area, is_point_inside_circle

def test_area():
    assert calculate_area(5) == 78.5398

def test_point_inside():
    assert is_point_inside_circle((3, 4), 10) == True