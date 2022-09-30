import sys

while True:
    ans = 'no'
    text = input()
    if text == '.':
        break
    stack = []
    flag = True
    for i in range(len(text)):
        if not text[i].isalpha():
            if text[i] == '(':
                stack.append(text[i])
            elif text[i] == ')':
                if not stack:
                    flag = False
                    break
                elif stack[-1] == '[':
                    break
                elif stack[-1] == '(':
                    stack.pop()
            elif text[i] == '[':
                stack.append(text[i])
            elif text[i] == ']':
                if not stack:
                    flag = False
                    break
                elif stack[-1] == '(':
                    break
                elif stack[-1] == '[':
                    stack.pop()
    if not stack and flag:
        ans = 'yes'
    print(ans)