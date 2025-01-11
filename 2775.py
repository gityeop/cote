import sys

input = sys.stdin.readlines()
N = int(input.pop(0))
memo = {}


def pivo(k, n):
    if (k, n) in memo:
        return memo[(k, n)]
    if k == 0:
        return n
    elif n == 1:
        return 1
    else:
        result = pivo(k, n - 1) + pivo(k - 1, n)
        memo[(k, n)] = result
        return result


for i in range(0, 2 * N, 2):
    k = int(input[i].strip())
    n = int(input[i + 1].strip())
    print(pivo(k, n))
