def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


N, K = map(int, input().split())
print(factorial(N) // (factorial(N - K) * factorial(K)))

import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


N, K = 20, 10

# 괄호 없는 경우
start_time = time.time()
for _ in range(100000):
    factorial(N) // (factorial(N - K) * factorial(K))
print("No extra parentheses:", time.time() - start_time)

# 괄호 추가된 경우
start_time = time.time()
for _ in range(100000):
    factorial(N) // ((factorial(N - K) * factorial(K)))
print("With extra parentheses:", time.time() - start_time)
