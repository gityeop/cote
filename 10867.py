import sys

input = sys.stdin.readlines()
nums = list(map(int, input[1].split()))
print(" ".join(map(str, sorted(set(nums)))))
