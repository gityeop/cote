n ,m = map(int, input().split())
a = []
b = []
for _ in range(n):
    r = list(map(int, input().split()))
    a.append(r)
for _ in range(n):
    r = list(map(int, input().split()))
    b.append(r)

for i in range(n):
    for j in range(m):
        a[i][j] += b[i][j]
    print(" ".join(map(str,(a[i]))))