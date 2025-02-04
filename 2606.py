import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

infected = [False] * n
infected[0] = True
q = deque([0])

while q:
    u = q.popleft()
    for v in adj[u]:
        if not infected[v]:
            infected[v] = True
            q.append(v)
print(infected.count(True) - 1)
