import sys
from collections import Counter

input = list(map(int, sys.stdin.readlines()))

n = input.pop(0)
print(round(sum(input) / n))
print(sorted(input)[n // 2])
freq = Counter(sorted(input)).most_common()
if len(freq) > 1 and freq[0][1] == freq[1][1]:
    print(freq[1][0])
else:
    print(freq[0][0])
print(max(input) - min(input))
