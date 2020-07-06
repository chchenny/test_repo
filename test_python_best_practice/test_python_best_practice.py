def fib(n: int) -> int:
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def my_add(num1: int, num2: int) -> int:
    return num1 + num2
