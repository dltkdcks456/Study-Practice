import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = [int(i) for i in input().rstrip()]
stack = []

for number in numbers:
    while stack and stack[-1] < number and K > 0:
        K -= 1
        stack.pop()
    stack.append(number)
while K > 0:
    K -= 1
    stack.pop()
print(''.join(map(str, stack)))