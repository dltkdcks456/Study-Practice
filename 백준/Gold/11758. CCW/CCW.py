point = []
for _ in range(3):
    point.append(list(map(int, input().split())))
vector1 = [point[1][0] - point[0][0], point[1][1] - point[0][1]]
vector2 = [point[2][0] - point[1][0], point[2][1] - point[1][1]]
direction = 0
check = vector1[0] * vector2[1] - vector1[1] * vector2[0]
if check > 0:
    print(1)
elif check < 0:
    print(-1)
else:
    print(0)