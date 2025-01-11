with open("1026.txt", "r") as file:
    input = file.readlines()
N = int(input[0])
A = list(map(int, input[1].split()))
B = list(map(int, input[2].split()))
m = []
for i in range(N):
    m.append(sorted(A)[i] * sorted(B, reverse=True)[i])
print(sum(m))
