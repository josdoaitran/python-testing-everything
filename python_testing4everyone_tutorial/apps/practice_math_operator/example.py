# please write a method to sum 2 params
def sum(a, b):
    return a + b
# please write a method to subtract 2 params
def subtract(a, b):
    return a - b

# please write unit test 2 above methods
def test_sum():
    assert sum(1, 2) == 3
    assert sum(2, 2) == 4
    assert sum(3, 2) == 5

    assert subtract(1, 2) == -1
    assert subtract(2, 2) == 0
    assert subtract(3, 2) == 1
    assert subtract(4, 2) == 2
    assert subtract(5, 2) == 3
    assert subtract(6, 2) == 4

# write unit test for substract method
def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(2, 2) == 0
    assert subtract(3, 2) == 1
    assert subtract(4, 2) == 2
    assert subtract(5, 2) == 3
    assert subtract(6, 2) == 4


