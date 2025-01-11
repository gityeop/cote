with open("2750.txt", "r") as file:
    input = file.readlines()
print(list(input))
N = int(input[0])
nums = list(map(int, [x for x in input[1:]]))
print(nums)
print("\n".join(map(str, sorted(nums))))