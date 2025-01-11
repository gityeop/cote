from collections import deque

with open("10866.txt", "r") as file:
    input = file.readlines()

N = int(input[0])
q = deque()

for i in range(1, N + 1):
    try:
        a = input[i].split()
        if a[1]:
            if a[0] == "push_back":
                q.append(a[1])
            else:
                q.appendleft(a[1])
    except:
        try:
            if a[0] == "front":
                print(q[0])
            elif a[0] == "back":
                print(q[-1])
            elif a[0] == "size":
                print(len(q))
            elif a[0] == "empty":
                if len(q) == 0:
                    print(1)
                else:
                    print(0)
            elif a[0] == "pop_back":
                print(q.pop())
            else:
                print(q.popleft())
        except:
            print("-1")
