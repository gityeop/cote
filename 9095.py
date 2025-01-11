import sys

input = sys.stdin.read()
dp = [0] * 12
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
data = input.split()
T = int(data[0])
results = []
for i in range(1, T + 1):
    n = int(data[i])
    results.append(dp[n])
print("\n".join(map(str, results)))
