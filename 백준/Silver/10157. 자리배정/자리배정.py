R, C = map(int, input().split())
goal = int(input())
area = [[0] * C for _ in range(R)]
dc = [1, 0, -1, 0] # 우, 하, 좌, 상
dr = [0, 1, 0, -1]
d = 0

step = 1
c = 0
r = 0

while step <= R * C:
    if r + dr[d] > R - 1 or c + dc[d] > C - 1:
        d += 1
    elif area[r + dr[d]][c + dc[d]] != 0:
        d += 1
    d = d % 4
    area[r][c] = step
    if step == goal:
        print(r + 1, c + 1)
        break
    r = r + dr[d]
    c = c + dc[d]
    step += 1
else:
    print(0)