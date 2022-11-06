import sys
input = sys.stdin.readline

N, Q, U, V = map(int, input().split())
K = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)
dp[1] = K[1]
for i in range(2, N + 1):
    dp[i] += dp[i - 1] + K[i]

for _ in range(Q):
    C, A, B = map(int, input().split())
    if C == 0:
        maxV = -float('inf')
        for i in range(A, B + 1):
            for j in range(i, B + 1):
                temp = 0
                if j == i:
                    temp = U * K[j]
                else:
                    temp = U * (dp[j] - dp[i - 1]) + V * (j - i)
                if temp > maxV:
                    maxV = temp
        print(maxV)

    else:
        diff = B - K[A]
        K[A] = B
        for d in range(A, N + 1):
            dp[d] += diff
