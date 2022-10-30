import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(r, c, ans=''):
    global flag
    if r == 1 and c == 1:
        if len(ans) == min(T1, T2):
            result.append(ans)
            flag = False
        elif text1[0] == text2[0]:
            flag = False
            result.append(text1[0] + ans)
        else:
            result.append(ans)
            flag = False
        return
    elif r != 1 and c != 1:
        if dp[r][c] > dp[r - 1][c] and dp[r][c] > dp[r][c - 1]:
            dfs(r - 1, c - 1, text1[r - 1] + ans)
            if not flag:
                return
        elif dp[r][c - 1] > dp[r - 1][c]:
            dfs(r, c - 1, ans)
            if not flag:
                return
        elif dp[r - 1][c] > dp[r][c - 1]:
            dfs(r - 1, c, ans)
            if not flag:
                return
        elif dp[r][c - 1] == dp[r - 1][c]:
            dfs(r, c - 1, ans)
            if not flag:
                return
            dfs(r - 1, c, ans)
            if not flag:
                return
    elif c == 1:
        if dp[r][1] == dp[r - 1][1]:
            dfs(r - 1, c, ans)
            if not flag:
                return
        else:
            dfs(r - 1, c, text1[r - 1] + ans)
            if not flag:
                return
    elif r == 1:
        if dp[1][c] == dp[1][c - 1]:
            dfs(r, c - 1, ans)
            if not flag:
                return
        else:
            dfs(r, c - 1, text2[c - 1] + ans)
            if not flag:
                return

text1 = input().rstrip()
text2 = input().rstrip()

T1 = len(text1)
T2 = len(text2)

dp = [[0] * (T2 + 1) for _ in range(T1 + 1)]

for r in range(1, T1 + 1):
    for c in range(1, T2 + 1):
        if text1[r - 1] == text2[c - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

result = []
flag = True
dfs(T1, T2)
print(dp[T1][T2])
print(result[0])