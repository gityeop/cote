import sys


def is_balenced(s):
    stack = []
    brackets = {")": "(", "]": "["}
    for char in s:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            if not stack or stack[-1] != brackets[char]:
                return "no"
            stack.pop()
    return "yes" if not stack else "no"


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    print("\n".join([is_balenced(line) for line in lines if line != "."]))
