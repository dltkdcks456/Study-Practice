import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
N = int(input())
ans = 0
for _ in range(N):
    u, v = map(int, input().split())
    cal = a * ((v - b) ** 2) + c
    if cal == u:
        ans += 1
print(ans)