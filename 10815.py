import sys
input = sys.stdin.readlines()
# with open("10815.txt", 'r') as file:
#     input = file.readlines()
N = int(input[0])
sgcard = set(map(int, input[1].split()))
M = int(input[2])
numcard = list(map(int, input[3].split()))

result = [1 if x in sgcard else 0 for x in numcard]
print(" ".join(map(str, result)))