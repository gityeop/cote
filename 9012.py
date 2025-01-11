import sys


def check_VPS(s):
    a = 0
    nums = map(lambda x: 1 if x == "(" else -1, s)
    for n in nums:
        a += n
        if a < 0:
            return "NO"

    if a > 0:
        return "NO"
    else:
        return "YES"


input = sys.stdin.readlines()
n = int(input[0])
for i in range(1, n + 1):
    print(check_VPS(input[i].strip()))
