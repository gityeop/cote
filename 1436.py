def shom(n):
    return "666" in str(n)


n = int(input())
count = 0
num = 666
while True:
    if shom(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1
