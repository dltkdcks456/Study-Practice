import sys
input = sys.stdin.readline

def serial(x):
    if x > stack[-1]:
        stack.append(x)
    else:
        start = 0
        end = len(stack) - 1
        while start <= end:
            mid = (start + end) // 2
            if stack[mid] > x:
                end = mid - 1
            elif stack[mid] < x:
                start = mid + 1
            else:
                break
        if stack[mid] == x:
            return
        elif stack[start] > x:
            stack[start] = x


N = int(input())
num = list(map(int, input().split()))
dp = [0] * N
stack = []
for i in num:
    if stack:
        serial(i)
    else:
        stack.append(i)
print(len(stack))