import sys

input = sys.stdin.readline
M = int(input())
S = set()
for i in range(M):
    command = input().strip().split()
    if len(command) == 2:
        a, b = command
        b = int(b)
        if a == "add":
            S.add(b)
        elif a == "remove":
            S.discard(b)
        elif a == "check":
            print(1 if b in S else 0)
        elif a == "toggle":
            if b in S:
                S.discard(b)
            else:
                S.add(b)
    else:
        a = command[0]
        if a == "all":
            S = set(range(1, 21))
        elif a == "empty":
            S.clear()
