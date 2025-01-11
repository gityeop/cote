import sys

input = sys.stdin.readlines()
N = int(input.pop(0).strip())
print("".join(sorted([i for i in input])))
