from calculator import divide


def test_divide_normal_numbers():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(10, 0)
    except ValueError as e:
        assert str(e) == 'Cannot divide by zero'
    else:
        assert False, 'Expected ValueError to be raised'