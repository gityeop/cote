import sys
input = sys.stdin.readline

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n)]
dp[0] = rgb[0]  # 첫 집은 그대로 시작

for i in range(1, n):
    dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])  # 빨강
    dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])  # 초록
    dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])  # 파랑

print(min(dp[n-1]))
