import sys

input = sys.stdin.read().splitlines()
n, m = map(int, input.pop(0).split())

one_pw = {}

for i in range(n):
    website, pw = input[i].split()
    one_pw[website] = pw

for i in range(n, n + m):
    print(one_pw[input[i]])
