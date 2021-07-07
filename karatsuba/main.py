def karatsuba(x, y):
    if (len(str(x)) == 1 or len(str(y)) == 1):
        return x * y
    n = max(len(str(x)), len(str(y)))
    power = int(n // 2)
    x1 = int(x // 10 ** power)
    x0 = int(x % 10 ** power)
    y1 = int(y // 10 ** power)
    y0 = int(y % 10 ** power)
    z0 = karatsuba(x0, y1)
    z2 = karatsuba(x1, y1)
    z = karatsuba((x0+x1), (y0 + y1)) - z0-z2
    res = z2 * 10 ** n + z * 10 ** power + z0
    return res


print(karatsuba(int(input()), int(input())))
