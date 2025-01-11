from collections import deque

N, K = map(int, input().split())

circle = deque([i for i in range(1, N + 1)])
result = []
while circle:
    circle.rotate(-K + 1)
    result.append(circle.popleft())
print("<" + ", ".join(map(str, result)) + ">")
