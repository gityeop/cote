import sys

input = sys.stdin.radlines()
N, B = map(int, input[0].split())


def matrix_mul(a):
    b = a
    mat_size = len(a)
    for id, i in enumerate(a):
        for idx, j in enumerate(i):
            b[id][idx] = j * a[idx][id]
    return b


for i in range(B):
    matrix_mul()
