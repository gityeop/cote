import sys
from itertools import combinations
input = sys.stdin.readlines()
N, M = map(int, input[0].split())
A = list(map(int, input[1].split()))
max_sum = 0
for combo in combinations(A, 3):
    combo_sum = sum(combo)
    if combo_sum == M:
        max_sum = combo_sum
        break
    elif combo_sum < M:
        max_sum = max(max_sum, combo_sum)
print(max_sum)