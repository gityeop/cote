import math
import sys

n = int(sys.stdin.readline())
for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    print(math.comb(n, m))
