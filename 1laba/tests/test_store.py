import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from store import calculate_store_items

def test_lamp_cost():
    assert calculate_store_items()['Лампа']['cost'] == 1134

def test_table_quantity():
    assert calculate_store_items()['Стол']['quantity'] == 54