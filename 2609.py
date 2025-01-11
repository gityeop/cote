import sys


# 최대공약수(Greatest Common Divisor, GCD)를 계산하는 함수
# 예시: a = 12, b = 18
def gcd(a, b):
    # b가 0이 될 때까지 반복합니다.
    while b:
        # a를 b로 나눈 나머지를 b에 저장하고, 이전의 b 값을 a에 저장합니다.
        # 예시 1: a = 12, b = 18 -> a % b = 12, a = 18, b = 12
        # 예시 2: a = 18, b = 12 -> a % b = 6, a = 12, b = 6
        # 예시 3: a = 12, b = 6 -> a % b = 0, a = 6, b = 0
        a, b = b, a % b
    # b가 0이 되면 a가 최대공약수입니다.
    # 예시: b가 0이 되었으므로 a (6)를 반환합니다.
    return a


# 최소공배수(Least Common Multiple, LCM)를 계산하는 함수
# 예시: a = 12, b = 18, gcd(a, b) = 6
def lcm(a, b):
    # 최소공배수는 두 수의 곱을 최대공약수로 나눈 값과 같습니다.
    # 예시: (12 * 18) // 6 = 216 // 6 = 36
    return (a * b) // gcd(a, b)


# 표준 입력에서 두 정수를 읽어옵니다.
a, b = map(int, sys.stdin.readline().strip().split())
# 예시 입력: 12 18
# a에 12가 저장되고, b에 18이 저장됩니다.

# 최대공약수를 계산합니다.
result_gcd = gcd(a, b)
# 최소공배수를 계산합니다.
result_lcm = lcm(a, b)

# 최대공약수를 출력합니다.
print(result_gcd)
# 예시 출력: 6
# 최소공배수를 출력합니다.
print(result_lcm)
# 예시 출력: 36
