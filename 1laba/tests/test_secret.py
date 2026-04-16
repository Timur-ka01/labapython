import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from secret import decrypt_message

def test_returns_string():
    assert isinstance(decrypt_message(), str)

def test_not_empty():
    assert len(decrypt_message()) > 0