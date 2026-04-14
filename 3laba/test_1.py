from one import f, p

def test_f():
    assert f([1, [2, [3, 4, [5]]]]) == 15

def test_p():
    assert p([1, [2, [3, 4, [5]]]]) == 15

def test_both_equal():
    assert f([1, [2, 3], 4]) == p([1, [2, 3], 4])