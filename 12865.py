# 입력 받기
N, K = map(int, input().split())
items = []

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

# DP 배열 초기화
dp = [0] * (K + 1)

# DP 알고리즘 실행
for W, V in items:
    for i in range(K, W - 1, -1):  # 큰 무게부터 시작해서 작은 무게로 내려가면서 계산
        dp[i] = max(dp[i], dp[i - W] + V)

# 배낭에 넣을 수 있는 물건들의 최대 가치 출력
print(dp[K])
