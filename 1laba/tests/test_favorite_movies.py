import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from favorite_movies import get_movies

def test_first_movie():
    assert get_movies()['first'] == 'Терминатор'

def test_last_movie():
    assert get_movies()['last'] == 'Назад в будущее'