from collections import deque

with open("10845.txt", "r") as file:
    input = file.readlines()

N = int(input[0])
q = deque()
for i in range(1, N + 1):
    a = input[i].strip().split()
    try:
        if a[1]:
            q.append(a[1])
    except:
        try:
            if a[0] == "pop":
                print(q.popleft())
            elif a[0] == "size":
                print(len(q))
            elif a[0] == "front":
                print(q[0])
            elif a[0] == "back":
                print(q[-1])
            elif a[0] == "empty":
                if len(q) == 0:
                    print(1)
                else:
                    print(0)
        except:
            print("-1")
    # q.put(item)
    # q.get()
    # q.empty()
    # q.qsize()
