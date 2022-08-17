import sys
N = int(sys.stdin.readline())
cnt = 0
i = 666
num = '666'
while cnt < N:
    if num in str(i):
        cnt += 1
    i += 1
print(i - 1)