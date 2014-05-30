#coding: utf-8
"""
1, 1, 2, 3, 5对于N>2的费氏数列来说，从第三个值起每一个值都是前两个之和
下面求的是第N个费氏数列的值
"""

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci1(n):
    """
    非递归做法
    """
    i = 0
    a, b = 0, 1
    while i < n:
        a, b = b, a+b
        yield a
        i += 1

if __name__ == "__main__":
    n = 3
    f = fibonacci(n)
    print f
    f1  = list(fibonacci1(n))[-1]
    print f1
