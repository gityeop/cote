import heapq
import sys

input = sys.stdin.read

data = input().split()

max_heap = []
min_heap = []
result=[]
for i in range(1, int(data[0])+1):
    num = int(data[i])
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else: heapq.heappush(min_heap, num)
    
    if min_heap and -max_heap[0] > min_heap[0]:
        max_val = heapq.heappop(max_heap)
        min_val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_val)
        heapq.heappush(min_heap, max_val)
    print(-max_heap[0])