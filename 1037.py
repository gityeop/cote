n = int(input())

a = list(map(int, input().split()))

if max(a) == min(a):
    print(a[0]**2)
else: print(max(a)*min(a))