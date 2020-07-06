import sys


def addition(a: float, b: float):
    return a + b


if __name__ == "__main__":
    num1 = sys.argv[0]
    num2 = sys.argv[1]
    print(addition(float(num1), float(num2)))
