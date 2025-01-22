import sys

input = sys.stdin.readlines()
n = int(input.pop(0))
dp_0 = [0] * (41)
dp_1 = [0] * (41)

dp_0[0] = 1
dp_0[1] = 0
dp_1[0] = 0
dp_1[1] = 1

for i in range(2, 41):
    dp_0[i] = dp_0[i - 1] + dp_0[i - 2]
    dp_1[i] = dp_1[i - 1] + dp_1[i - 2]

for i in range(n):
    num = int(input[i])
    print(dp_0[num], dp_1[num])
