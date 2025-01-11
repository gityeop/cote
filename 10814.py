import sys

input = sys.stdin.readlines()
N = int(input.pop(0).strip())
l = []
for i in range(N):
    a, b = input[i].split()
    a = int(a)
    l.append((a, b))
l = sorted(l, key=lambda x: x[0])
for i in l:
    print(i[0], i[1])
