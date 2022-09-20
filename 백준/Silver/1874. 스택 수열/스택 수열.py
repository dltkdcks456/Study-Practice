n = int(input())
stack = []
last = 0
result = []
for i in range(n):
    data = int(input())
    if stack:
        if stack[-1] <= data:
            while stack[-1] != data:
                last += 1
                stack.append(last)
                result.append('+')
            stack.pop()
            result.append('-')
        else:
            print('NO')
            break
    else:
        if data >= last:
            last += 1
            stack.append(last)
            result.append('+')
            while stack[-1] != data:
                last += 1
                stack.append(last)
                result.append('+')
            stack.pop()
            result.append('-')
        else:
            print('No')
            break
else:
    print('\n'.join(result))