import sys

n = int(sys.stdin.readline())
counts = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(1, 10000):
    for _ in range(counts[i]):
        sys.stdout.write(str(i) + "\n")
