N = int(input())
maxV = 0
max_li = []

for n in range(N, 0, -1):
    li = [N, n]
    while li[-1] >= 0:
        li.append(li[-2] - li[-1])
    cnt = len(li)
    if maxV < cnt - 1:
        maxV = cnt - 1
        max_li = li
print(maxV)
print(*max_li[:maxV])