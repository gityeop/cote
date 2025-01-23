import sys


def is_right_triangle(sides):
    a, b, c = sorted(sides)
    return a * a + b * b == c * c if a > 0 else False


for line in sys.stdin:
    sides = list(map(int, line.strip().split()))
    if sides == [0, 0, 0]:
        break
    print("right" if is_right_triangle(sides) else "wrong")
