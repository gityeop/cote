n = int(input())
dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(3, n + 1):
    if dp[i - 3] != float("inf"):
        dp[i] = min(dp[i], dp[i - 3] + 1)

for i in range(5, n + 1):
    if dp[i - 5] != float("inf"):
        dp[i] = min(dp[i], dp[i - 5] + 1)

if dp[n] == float("inf"):
    print(-1)
else:
    print(dp[n])
