import sys

s = ["Fizz", "Buzz", "FizzBuzz"]
input = sys.stdin.readlines()
n = 0
for i in range(3):
    if input[i].strip() in s:
        pass
    else:
        n = int(input[i].strip())
    n += 1
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
