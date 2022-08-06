T = int(input())
area_set = set()

def points(x, y):
    for i in range(10):
        for j in range(10):
            area_set.add((x + i, y + j))

for n in range(T):
    x, y = map(int, input().split())
    points(x, y)

print(len(area_set))
