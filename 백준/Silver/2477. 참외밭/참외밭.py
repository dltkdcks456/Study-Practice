N = int(input())
li = []
for _ in range(6):
    li.append(list(map(int, input().split())))
D = [1, 4, 2, 3]
d = D.index(li[0][0]) - 1
maxc = 0
maxr = 0
flag = False
delete_area = 0
for i in range(len(li)):
    d = (d + 1) % 4
    if li[i][0] != D[d] and flag == False:
        delete_area = li[i][1] * li[i - 1][1]
        flag = True
        
    if li[i][0] == 1 or li[i][0] == 2:
        if li[i][1] > maxr:
            maxr = li[i][1]
    else:
        if li[i][1] > maxc:
            maxc = li[i][1]

if flag == False:
    delete_area = li[0][1] * li[-1][1]

total = maxr * maxc
ans = (total - delete_area) * N
print(ans)