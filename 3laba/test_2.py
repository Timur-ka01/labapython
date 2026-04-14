from two import f, p

def test_f_runs():
    try:
        f(1.0, 1.0)
        assert True
    except:
        assert False

def test_p_runs():
    try:
        p(1.0, 1.0, 1)
        assert True
    except:
        assert False