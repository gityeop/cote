import sys

input = sys.stdin.readlines()
n = int(input.pop(0))
times = sorted(list(map(int, input[0].split())))
result = 0
for i in range(n):
    result += sum(times[: i + 1])
print(result)
