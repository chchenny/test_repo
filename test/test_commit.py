import sys


def my_add(a: int, b: int):
    return a + b


if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print(my_add(num1, num2))
