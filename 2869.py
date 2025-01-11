import sys
import math

input = sys.stdin.read()
A, B, V = map(int, input.strip().split())
print(math.ceil((V - B) / (A - B)))
