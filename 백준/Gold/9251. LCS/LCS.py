import sys

text1 = sys.stdin.readline().rstrip()
text2 = sys.stdin.readline().rstrip()

N = len(text1)
M = len(text2)
Z = [[0] * (N + 1) for _ in range(M + 1)]
for r in range(1, M + 1):
    for c in range(1, N + 1):
        if text1[c - 1] == text2[r - 1]:
            Z[r][c] = Z[r - 1][c - 1] + 1
        else:
            Z[r][c] = max(Z[r - 1][c], Z[r][c - 1])
print(Z[M][N])