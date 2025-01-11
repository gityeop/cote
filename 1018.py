import sys

input = sys.stdin.readlines()
N, M = map(int, input.pop(0).split())
WB = ["WBWBWBWB", "BWBWBWBW"]
BW = ["BWBWBWBW", "WBWBWBWB"]
WB = WB * 4
BW = BW * 4
board = []
for i in range(N):
    board.append(input[i].strip())
result = []
for i in range(N - 7):
    for j in range(M - 7):
        part = [board[i : i + 8][k][j : j + 8] for k in range(8)]
        WB_count = 0
        BW_count = 0
        for k in range(8):
            for l in range(8):
                if part[k][l] != WB[k][l]:
                    WB_count += 1
                if part[k][l] != BW[k][l]:
                    BW_count += 1
        min_count = min(WB_count, BW_count)
        result.append(min_count)
print(min(result))
