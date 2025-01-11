import sys

input = list(map(int, sys.stdin.read().splitlines()))
n = input.pop(0)
nums = [i for i in range(1, n + 1)]
stack = []
result = []
while True:
    if nums and nums[0] <= input[0]:
        stack.append(nums.pop(0))
        result.append("+")
    elif stack and stack[-1] > input[0]:
        result = ["NO"]
        break
    if stack and stack[-1] == input[0]:
        stack.pop()
        input.pop(0)
        result.append("-")
    if not stack and not nums:
        break
print("\n".join(result))
