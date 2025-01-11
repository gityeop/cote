s = input()
sn = 0
f = 69 - ord(s[0])
try:
    if s[1] == "+":
        f+=0.3
    elif s[1] == '-':
        f-=0.3
except: f = 0

print(float(f))