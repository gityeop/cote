N = int(input())
a = [0] * 501


def factorial(n):
    if n == 0:
        return 1
    if a[n] != 0:
        return a[n]
    a[n] = n * factorial(n - 1)
    return n * factorial(n - 1)


f = factorial(N)
count = 0
for s in reversed(str(f)):
    if s == "0":
        count += 1
    else:
        break
print(count)
