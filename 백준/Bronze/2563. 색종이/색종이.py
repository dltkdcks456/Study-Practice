T = int(input())
area_set = list()

for n in range(T):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            area_set.append((x + i, y + j))

print(len(set(area_set)))