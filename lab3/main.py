# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def fib(n):
    if n < 2:
        return n
    else:
        return n + fib(n-1)


def fac(n):
    if n <= 1:
        return 1
    else:
        return n * fac(n - 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputNum = int(input())
    print(fib(inputNum))
