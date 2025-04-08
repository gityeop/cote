n = int(input())

# 1, 3(1+2), 5(3+2), 11(5+6), 21(11+10), 43(21+22), 85(43+42), 171(85+86)
dp = [0] * (n + 1)
dp[0] = 1
for i in range(1, n+1):
    dp[i] = dp[i-1] + 2*dp[i-2]
print(dp[n]%10007)
