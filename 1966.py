import sys
from collections import deque

input = sys.stdin.readlines()
N = int(input[0])
results = []
for i in range(N):
    doc_size, doc_pos = map(int, input[2 * i + 1].split())
    prior = list(map(int, input[2 * i + 2].split()))
    q = deque((priority, idx) for idx, priority in enumerate(prior))
    order = 0
    while q:
        current = q.popleft()
        if any(current[0] < doc[0] for doc in q):
            q.append(current)
        else:
            order += 1
            if current[1] == doc_pos:
                results.append(order)
                break
for result in results:
    print(result)
