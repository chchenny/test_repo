import sys

from test_python_best_practice.test_python_best_practice import fib, my_add

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    print(fib(n))
    print(my_add(n, m))
