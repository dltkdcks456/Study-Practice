T = int(input())
area_set = set()

for n in range(T):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            area_set.add((x + i, y + j))

print(len(area_set))