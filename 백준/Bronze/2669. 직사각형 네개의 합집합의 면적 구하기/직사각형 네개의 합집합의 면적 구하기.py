area = [[0] * 101 for _ in range(101)]
maxV = 0
minV = 101
for _ in range(4):
    pos = list(map(int, input().split()))
    if pos[3] > maxV:
        maxV = pos[3]
    if pos[1] < minV:
        minV = pos[1]
    for i in range(pos[0], pos[2]):
        for j in range(pos[1], pos[3]):
            area[j][i] = 1
total = 0
for k in range(minV, maxV):
    total += sum(area[k])
print(total)