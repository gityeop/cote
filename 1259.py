import sys


def reverse(s):
    return s[::-1]


input = sys.stdin.readlines()
i = 0
while True:
    if input[i].strip() == "0":
        break
    elif input[i].strip() == input[i].strip()[::-1]:
        print("yes")
    else:
        print("no")
    i += 1
