from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for _ in range(K):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    W = int(input())

    queue = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = time[i]

    while queue:
        current = queue.popleft()
        for next in graph[current]:
            indegree[next] -= 1
            dp[next] = max(dp[next], dp[current] + time[next])
            if indegree[next] == 0:
                queue.append(next)

    print(dp[W])
    