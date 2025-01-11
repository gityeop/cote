import sys


def sorted2(coin):
    if k // coin >= 1:
        return coin


input = sys.stdin.readlines()
n, k = map(int, input.pop(0).split())
input = sorted(list(map(int, input)), reverse=True)
coins = list(filter(sorted2, input))
count = 0
for coin in coins:
    count += k // coin
    k -= coin * (k // coin)
print(count)
