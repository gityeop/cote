import sys

input = sys.stdin.readlines()
k, n = map(int, input.pop(0).strip().split())
lan_cables = list(map(int(line.strip()) for line in input))
start, end = 1, max(lan_cables)
result = 0
while start <= end:
    mid = (start + end) // 2
    lines = sum([cable // mid for cable in lan_cables])
    if lines >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)
