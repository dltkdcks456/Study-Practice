import sys
N = int(sys.stdin.readline())
ans = 0
for i in range(1, N):
    if i + sum(list(map(int,str(i)))) == N:
        ans = i
        break
print(ans)