import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from songs_list import calculate_song_times

def test_first_three():
    assert calculate_song_times()['first_three'] == 14.93

def test_second_three():
    assert calculate_song_times()['second_three'] == 13.0