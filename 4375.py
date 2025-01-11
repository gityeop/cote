import sys


input = sys.stdin.readlines()
nums = list(map(int, [line.strip() for line in input]))
result = 1
idx = 0
for x in nums:
    while result%x != 0:
      result += 10**(idx+1)
      idx+=1
    print(len(str(result)))
    result = 1
    idx =0