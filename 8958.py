import sys

input = sys.stdin.readlines()
N = int(input[0])

# breakpoint()
for i in range(1, N + 1):
    streak = 0
    result = 0
    for a in input[i]:
        if a == "O":
            result += 1 + streak
            streak += 1
        else:
            streak = 0
    print(result)
