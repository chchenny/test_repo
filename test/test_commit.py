import sys


def addition(a: int, b: int):
    return a + b


if __name__ == "__main__":
    num1 = sys.argv[0]
    num2 = sys.argv[1]
    print(addition(int(num1), int(num2)))
