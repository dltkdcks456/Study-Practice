import sys
input = sys.stdin.readline

def hanoi(n, A, B, C):  # 시작, 종료, 경유지
    global cnt
    if n == 1:
        print(A, B)
        return
    hanoi(n - 1, A, C, B)   # 우선 경유지에 n-1개를 가져다 놓아야함
    print(A, B)         # 시작점에서 도착점에 가장 큰 것을 하나두고
    hanoi(n - 1, C, B, A)   # 경유지에 있던 n-1개의 원판을 도착점으로


N = int(input())
dp = [0] * (N + 1)
dp[1] = 1
for i in range(2, N + 1):
    dp[i] = 2 * dp[i - 1] + 1
print(dp[N])
if N <= 20:
    hanoi(N, 1, 3, 2)