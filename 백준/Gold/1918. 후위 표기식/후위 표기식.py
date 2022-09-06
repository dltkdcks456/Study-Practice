cal = input()
score = {'*' : (2, 2), '/' : (2, 2), '+': (1, 1), '-' : (1, 1), '(' : (3, 0)}
stack = []
for i in cal:
    if i not in '*-/+()':
        print(i, end = '')
    else:
        if stack:
            if i != ')':
                while stack and score[stack[-1]][1] >= score[i][0] and stack[-1] != '(':
                    print(stack.pop(-1), end='')
                stack.append(i)
            else:
                while stack[-1] != '(':
                    print(stack.pop(-1), end='')
                stack.pop(-1)
        else:
            stack.append(i)

while stack:
    print(stack.pop(-1), end='')