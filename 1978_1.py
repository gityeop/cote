import sys

input = sys.stdin.readlines()


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input[0])
numbers = map(int, input[1].split())
count = 0

for number in numbers:
    if is_prime(number):
        count += 1

print(count)
