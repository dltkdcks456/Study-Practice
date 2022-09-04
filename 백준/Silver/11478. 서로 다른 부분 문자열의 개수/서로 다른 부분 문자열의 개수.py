import sys
text = sys.stdin.readline().rstrip()
N = len(text)
ans = set()
for i in range(N):
    for j in range(N - i):
        ans.add(text[j : j + i + 1])
print(len(ans))