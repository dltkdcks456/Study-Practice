import sys

input=sys.stdin.readline
N = int(input())
M = int(input())
S = input()

P = 'IOI'
idx = 0
cnt = 0
num = []
while idx <= M - 2:
    flag = True
    if S[idx: idx + 3] == P:
        cnt += 1
        idx += 2
        flag = False
    else:
        num.append(cnt)
        cnt = 0
        idx += 1
else:
    if not flag:
        num.append(cnt)
ans = 0
for i in num:
    if i >= N:
        ans += i - N + 1

print(ans)