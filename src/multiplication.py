def mul(a,b):
    return a * b

def test_mul():
    assert mul(1, 2) == 2
    assert mul(1, -1) == -1
    assert mul(0, 1) == 0
    assert mul(1, 0) == 0
    assert mul(0, 0) == 0
    assert mul(2, 2) == 4
    assert mul(2, -2) == -4
    assert mul(-2, 2) == -4
    assert mul(-2, -2) == 4
    assert mul(3, 3) == 9
    assert mul(3, -3) == -9
    assert mul(-3, 3) == -9
    assert mul(-3, -3) == 9
    assert mul(4, 4) == 16
    assert mul(4, -4) == -16
    assert mul(-4, 4) == -16
    assert mul(-4, -4) == 16
    assert mul(5, 5) == 25
    assert mul(5, -5) == -25
    assert mul(-5, 5) == -25
    assert mul(-5, -5) == 25
    assert mul(6, 6) == 36
    assert mul(6, -6) == -36
    assert mul(-6, 6) == -36
    assert mul(-6, -6) == 36
    assert mul(7, 7) == 49
    assert mul(7, -7) == -49
    assert mul(-7, 7) == -49
    assert mul(-7, -7) == 49
    assert mul(8, 8) == 64
    assert mul(8, -8) == -64
    assert mul(-8, 8) == -64
    assert mul(-8, -8) == 64
    assert mul(9, 9) == 81
    assert mul(9, -9) == -81
    assert mul(-9, 9) == -81
    assert mul(-9, -9) == 81
    assert mul(10, 10) == 100
    assert mul(10, -10) == -100