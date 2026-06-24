def uniquePaths(m, n):
    dp = [1] * n

    for i in range(m - 1):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[-1]

m = 3
n = 2

print("Unique Paths =", uniquePaths(m, n))
