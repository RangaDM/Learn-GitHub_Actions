def sub(a,b):
    return a - b

def test_sub():
    assert sub(1, 2) == -1
    assert sub(1, -1) == 2
    assert sub(0, 1) == -1
    assert sub(1, 0) == 1
    assert sub(0, 0) == 0
    assert sub(2, 2) == 0
    assert sub(2, -2) == 4
    assert sub(-2, 2) == -4
    assert sub(-2, -2) == 0
    assert sub(3, 3) == 0
    assert sub(3, -3) == 6
    assert sub(-3, 3) == -6
    assert sub(-3, -3) == 0
    assert sub(4, 4) == 0
    assert sub(4, -4) == 8
    assert sub(-4, 4) == -8
    assert sub(-4, -4) == 0
    assert sub(5, 5) == 0
    assert sub(5, -5) == 10
    assert sub(-5, 5) == -10
    assert sub(-5, -5) == 0
    assert sub(6, 6) == 0
    assert sub(6, -6) == 12
    assert sub(-6, 6) == -12
    assert sub(-6, -6) == 0
    assert sub(7, 7) == 0
    assert sub(7, -7) == 14
    assert sub(-7, 7) == -14
    assert sub(-7, -7) == 0
    assert sub(8, 8) == 0
    assert sub(8, -8) == 16
    assert sub(-8, 8) == -16
    assert sub(-8, -8) == 0
    assert sub(9, 9) == 0
    assert sub(9, -9) == 18
    assert sub(-9, 9) == -18
    assert sub(-9, -9) == 0
    assert sub(10, 10) == 0
    assert sub(10, -10) == 20