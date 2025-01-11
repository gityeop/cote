import sys


def rnd(n):
    return round(n + 0.1) if n - int(n) >= 0.5 else round(n - 0.1)


input = sys.stdin.readlines()

n = int(input.pop(0))
if n == 0:
    print(0)
    sys.exit()
scores = sorted(list(map(int, input)))
k = rnd(n * 0.15)
scores = scores[int(k) : int(n - k)]
print(rnd(sum(scores) / len(scores)))
