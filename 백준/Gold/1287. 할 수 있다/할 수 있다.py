li1 = input()
li = []
s = ''
for i in range(len(li1)):
    if li1[i].isdigit():
        if i == len(li1) - 1:
            s += li1[i]
            li.append(s)
        else:
            s += li1[i]
    else:
        if s:
            li.append(s)
            s = ''
            li.append(li1[i])
        else:
            li.append(li1[i])
            
token = {'+': (1, 1), '-': (1, 1), '(': (0, 3), '/': (2, 2), '*': (2, 2)}
stack = []
postfix = []
c_d = 0
c_nd = 0
flag = True
for i in li:
    if i.isdigit():
        postfix.append(int(i))
        c_d += 1
    else:
        try:
            if i == '(':
                stack.append(i)
            elif i in '+-':
                while stack and token[stack[-1]][0] >= 1:
                    postfix.append(stack.pop())
                stack.append(i)
                c_nd += 1
            elif i in '/*':
                while stack and token[stack[-1]][0] >= 2:
                    postfix.append(stack.pop())
                stack.append(i)
                c_nd += 1
            else:
                if stack and stack[-1] == '(':
                    print('ROCK')
                    flag = False
                    break
                else:
                    while stack and stack[-1] != '(':
                        postfix.append(stack.pop())
                    stack.pop()
        except:
            print('ROCK')
            flag = False
            break

if flag != False:
    while stack:
        if '(' in stack:
            print('ROCK')
            flag = False
            break
        else:
            postfix.append(stack.pop())
    else:
        if c_nd >= c_d:
            print('ROCK')
            flag = False

if flag:
    stack1 = []
    for k in postfix:
        if str(k).isdigit():
            stack1.append(k)
        else:
            try:
                first = stack1.pop()
                second = stack1.pop()
                if k == '+':
                    stack1.append(second + first)
                elif k == '-':
                    stack1.append(second - first)
                elif k == '*':
                    stack1.append(second * first)
                elif k == '/':
                    if first == 0:
                        flag = False
                        break
                    else:
                        stack1.append(second // first)
            except:
                print('ROCK')
                break
    if flag:
        print(stack1[-1])
    else:
        print('ROCK')