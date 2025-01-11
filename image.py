def change_to_box(numlist):
    result = list(
        map(lambda x: x[1] * "□" if x[0] % 2 == 1 else x[1] * "■", enumerate(numlist))
    )
    return result


with open("image.txt", "r") as file:
    input = file.readlines()

for i in range(len(input)):
    num_list = list(map(int, list(input[i].split(","))))
    result = change_to_box(num_list)
    a = "".join(result)
    if len(a) < 18:
        a = a + ("■" * (18 - len(a)))
    print(a)
