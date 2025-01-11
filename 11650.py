with open("11650.txt", "r") as file:
    input = file.readlines()
N = int(input[0])
points = []
for i in range(1, N + 1):
    x, y = map(int, input[i].split())
    points.append((x, y))

points.sort(key=lambda point: (point[0], point[1]))

for x, y in points:
    print(x, y)
