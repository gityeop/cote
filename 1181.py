import sys

with open("1181.txt", "r") as file:
    input = file.readlines()
input = sys.stdin.readlines()
N = int(input[0])
input = map(lambda x: x.strip(), set(input[1:]))
print("\n".join(sorted(input, key=lambda x: (len(x), x))))
