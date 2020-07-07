import sys

from test_python_best_practice.test_python_best_practice import fib

if __name__ == "__main__":
    n = int(sys.argv[1])
    print(fib(n))
