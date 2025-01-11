from collections import deque

with open("1406.txt", "r") as file:
    input = file.readlines()
s = input[0].strip()
N = int(input[1])
front = deque(s)
end = deque()

for i in range(2, N + 2):
    command = input[i].split()
    if command[0] == "P":
        front.append(command[1])
    elif command[0] == "L" and front:
        end.appendleft(front.pop())
    elif command[0] == "D" and end:
        front.append(end.popleft())
    elif command[0] == "B" and front:
        front.pop()

print("".join(front) + "".join(end))
