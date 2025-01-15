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
"""
Dynamic Programming이란?
큰 문제를 작은 하위 문제로 나누어 해결하는 알고리즘 설계 기법
이미 계산한 결과를 메모리에 저장하여 재사용 (Memoization)
중복 계산을 피해 실행 시간을 단축
이 문제에서 DP 활용
dp[i]: i킬로그램을 만들 수 있는 최소 봉지 개수를 저장
작은 무게부터 차례로 계산하여 큰 무게의 최적해를 구함
3kg, 5kg 봉지로 만들 수 있는 모든 경우의 수를 효율적으로 탐색

DP(동적 계획법) 문제인지 판단하는 주요 특징

1. 최적 부분 구조 (Optimal Substructure)
- 큰 문제가 작은 문제들로 나누어질 수 있음
예: dp[i]가 dp[i-3]과 dp[i-5]를 통해 계산됨

2. 중복되는 부분 문제 (Overlapping Subproblems)
- 동일한 작은 문제들이 반복적으로 나타남
예시 코드에서 볼 수 있듯이:

3. 최적화 문제
"최소" 봉지 개수를 구하는 등의 최적값을 찾는 문제
코드에서 보이는 min() 사용이 이를 나타냄

4. 상태 정의가 가능
각 상태(state)를 명확하게 정의할 수 있음
예: dp[i]는 i킬로그램을 만들 때 필요한 최소 봉지 수를 의미

"""
