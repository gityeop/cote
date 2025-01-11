import sys
input = sys.stdin.readlines()
N = int(input[0])
def str_to_int(s):
    return ord(s)-96
A = map(str_to_int, input[1].strip())
n=0
result = 0
for a in A:
    result += a*31**n
    n += 1
print(result % 1234567891)