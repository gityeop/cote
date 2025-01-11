with open('10828.txt','r') as file:
    input = file.readlines()

N = int(input[0])
stack = []
for i in range(1, N+1):
    a = input[i].strip().split()
    try:
        if a[1]:
            stack.append(a[-1])
    except:
        if a[0] == 'top':
            try: print(stack[-1]) 
            except: print("-1")
        elif a[0] == 'size':
            print(len(stack))
        elif a[0] == 'empty':
            if stack == []:
                print("1")
            else: print("0")
        else:
            try: print(stack.pop())

            except: print("-1")
        
