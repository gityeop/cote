with open('input.txt', 'r') as file:
  lines = file.readlines()
N = int(lines[0])
T_list= list(map(int,list(lines[1].split())))
T, P = map(int, list(lines[2].split()))
count = 0
for a in T_list:
  Q = (a-1)//T + 1
  count+=Q
c, d = N//P, N%P
print(count)
print(c, d)
  