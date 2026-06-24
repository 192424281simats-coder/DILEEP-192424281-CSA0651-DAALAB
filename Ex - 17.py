def tower(poured, row, glass):
    dp = [[0]*100 for _ in range(100)]
    dp[0][0] = poured

    for i in range(row):
        for j in range(i+1):
            extra = max(0, (dp[i][j]-1)/2)
            dp[i+1][j] += extra
            dp[i+1][j+1] += extra

    return min(1, dp[row][glass])

print(tower(2, 1, 1))
