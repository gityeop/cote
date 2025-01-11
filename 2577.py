import sys
from collections import Counter

input = sys.stdin.read()
a, b, c = map(int, input.split())
mul = a * b * c
count = Counter(str(mul))
for i in range(10):
    if count[str(i)]:
        print(count[str(i)])
    else:
        print("0")
