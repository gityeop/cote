a = int(input())
c = 0

for i in range(max(1, a-9*len(str(a))), a):
  cons = i + sum(map(int, str(i)))
  if cons == a:
    c = i
    break
print(c)
    


N = int(input())
result = 0

for i in range(1, N + 1):
    decomposition_sum = i + sum(map(int, str(i)))
    
    if decomposition_sum == N:
        result = i
        break

print(result)
