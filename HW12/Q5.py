# Hsuan-You Lin Module 10 Problem Set Question 5.
def karatsuba(x, y):
    a, b = x // 100, x % 100
    c, d = y // 100, y % 100

    ac = a * c
    print("\n<In Karatsuba algorithm> \na * c = ", ac)
    bd = b * d
    print("b * d = ", bd)
    abcd = (a+b) * (c+d)
    print("(a + b) * (c + d) = ", abcd)
    result = ac * 10000 + (abcd - ac - bd) * 100 + bd

    return result

if __name__ == "__main__" :
    x = 5822
    y = 4104
    print("Input Number: \n X = ", x, "; Y = ", y)
    print("\nExpected X * Y = ", x*y)
    ans = karatsuba(x, y)
    print("\n<After Karatsuba algorithm> \nX * Y = ", ans)
