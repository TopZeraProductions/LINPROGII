def hm(arg):
    pass

def test_hm1():
    assert hm(70) == (1, 10)

def test_hm2():
    assert hm(70) == (0, 30)

def test_hm3():
    try:
        hm('123')
        assert False
    except ValueError:
        pass
