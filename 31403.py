import sys

input = sys.stdin.read()

a, b, c = map(int, input.split())

print(a + b - c)
print(int(str(a) + str(b)) - c)
