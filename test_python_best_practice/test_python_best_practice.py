def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def my_add(a: int, b: int) -> int:
    return a + b
