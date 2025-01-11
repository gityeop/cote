with open('1978_input.txt', 'r') as file:
  lines=file.readlines()
print(lines)

N = int(lines[0])
count=0
for i in range(N):
  a = int(lines[1].split()[i])
  for j in range(N-i-1):
    b = int(lines[1].split()[i+j+1])
    if b%a != 0:
      count+=1
    
print(count)