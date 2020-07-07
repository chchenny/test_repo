from test_python_best_practice.test_python_best_practice import fib, my_add


def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(10) == 55


def test_my_add() -> None:
    assert my_add(1, 1) == 2
    assert my_add(0, 5) == 5
    assert my_add(12, 40) == 52
    assert my_add(-2, 2) == 0
