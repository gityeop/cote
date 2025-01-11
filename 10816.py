import sys
from collections import Counter

input = sys.stdin.readlines()
sg = list(map(int, input[1].split()))
counter = Counter(sg)
criteria = list(map(int, input[3].split()))
a = []
for item in criteria:
    a.append(counter[item])
print(" ".join(map(str, a)))
