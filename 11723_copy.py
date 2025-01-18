import sys

input = sys.stdin.readline
M = int(input())
commands = []
check_positions = []
S = set()

# 모든 명령어와 check 위치 저장
for i in range(M):
    command = input().strip().split()
    commands.append(command)
    if len(command) == 2 and command[0] == "check":
        check_positions.append((i, int(command[1])))

# 각 check 위치까지의 명령어 실행
for check_pos, check_num in check_positions:
    S = set()  # 매 check마다 초기화

    # check 위치까지의 명령어 실행
    for i in range(check_pos):
        command = commands[i]

        if len(command) == 2:
            op, num = command
            num = int(num)

            if op == "add":
                S.add(num)
            elif op == "remove":
                S.discard(num)
            elif op == "toggle":
                if num in S:
                    S.discard(num)
                else:
                    S.add(num)
        else:
            op = command[0]
            if op == "all":
                S = set(range(1, 21))
            elif op == "empty":
                S.clear()

    # check 결과 출력
    print(1 if check_num in S else 0)
