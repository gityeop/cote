import sys


def sort_by_two_criteria(data, key1, key2, reverse1=False, reverse2=False):
    return sorted(
        data, key=lambda item: (key1(item), key2(item)), reverse=(reverse1, reverse2)
    )


input = sys.stdin.readlines()
N = int(input.pop(0))
result = [0] * N
top = (0, 0)
for i in range(N):
    data_now_x = int(input[i].split()[0])
    data_now_y = int(input[i].split()[1])
    result[i] = (data_now_x, data_now_y)

result = sort_by_two_criteria(result, lambda x: x[0], lambda x: x[1])
for i in range(N):
    print(result[i][0], result[i][1])
