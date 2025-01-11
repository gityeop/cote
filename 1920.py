import sys
with open("1920.txt", "r") as file:
  input = file.readlines()
N = int(input[0])
A = list(map(int,input[1].split()))
M = int(input[2])
M_list = list(map(int, input[3].split()))

result = map(lambda x: 1 if x in A else 0, M_list)
print("\n".join(list(map(str,result))))