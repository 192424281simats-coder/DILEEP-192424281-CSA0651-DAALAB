def findWays(m, n, N, i, j):
    if N == 0:
        return 0

    ways = 0

    if i == 0:
        ways += 1
    if i == m - 1:
        ways += 1
    if j == 0:
        ways += 1
    if j == n - 1:
        ways += 1

    if N > 1:
        ways += findWays(m, n, N - 1, i, j)

    return ways

m = 2
n = 2
N = 2
i = 0
j = 0

print("Ways =", findWays(m, n, N, i, j))
