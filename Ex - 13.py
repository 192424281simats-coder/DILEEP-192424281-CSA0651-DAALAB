def climb(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = 4
print("Ways =", climb(n))
