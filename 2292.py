import sys

n = int(sys.stdin.read())
for i in range(1, n + 1):
    if n == 1:
        print(1)
        break
    if (3 * i * i - 9 * i + 8 <= n) and (3 * (i + 1) * (i + 1) - 9 * (i + 1) + 8 > n):
        print(i)
        break
