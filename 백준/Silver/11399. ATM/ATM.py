import sys

N = int(input())
data = sorted(list(map(int, input().split())))
ans = data[0]
for i in range(1, len(data)):
    data[i] += data[i - 1]
    ans += data[i]
print(ans)