N = int(input())
li = [list(map(int, input().split())) for _ in range(6)]

D = [1, 4, 2, 3]
d = D.index(li[0][0]) - 1
maxc = maxr = del_a = 0
flag = False
for i in range(6):
    d = (d + 1) % 4
    if li[i][0] != D[d] and flag == False:
        del_a = li[i][1] * li[i - 1][1]
        flag = True
        
    if li[i][0] == 1 or li[i][0] == 2:
        if li[i][1] > maxr:
            maxr = li[i][1]
    else:
        if li[i][1] > maxc:
            maxc = li[i][1]

if flag == False:
    del_a = li[0][1] * li[-1][1]

total = maxr * maxc
ans = (total - del_a) * N
print(ans)