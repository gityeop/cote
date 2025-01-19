import sys

input = sys.stdin.read().splitlines()

n, m = map(int, input.pop(0).split())
hear = set()
see = set()
result = []
for i in range(n):
    hear.add(input.pop(0))

for i in range(m):
    see.add(input.pop(0))
result = hear & see
print(len(result))
print("\n".join(sorted(result)))
