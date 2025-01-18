import sys

input = sys.stdin.readlines()
N, M = map(int, input.pop(0).split())

name_to_num = {}
pokemon_list = [""]

for i, name in enumerate(input[:N], 1):
    name = name.strip()
    name_to_num[name] = i
    pokemon_list.append(name)

for query in input[N:]:
    query = query.strip()
    if query.isdigit():
        print(pokemon_list[int(query)])
    else:
        print(name_to_num[query])
