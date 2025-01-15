n = int(input())
dp = [float("inf")] * (n + 1)
# dp[i]: i kg을 만들 수 있는 최소 봉지 개수
dp[0] = 0

for i in range(3, n + 1):
    if dp[i - 3] != float("inf"):
        dp[i] = min(dp[i], dp[i - 3] + 1)

for i in range(5, n + 1):
    if dp[i - 5] != float("inf"):
        dp[i] = min(dp[i], dp[i - 5] + 1)  # 5kg 봉지 사용 시의 최소값 계산

if dp[n] == float("inf"):  # 만들 수 없는 경우
    print(-1)
else:
    print(dp[n])  # 최소 봉지 개수 출력
