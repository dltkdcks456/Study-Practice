import sys
sys = sys.stdin.readline

def cut(x, y, size):
    init_V = paper[x][y]
    flag = True
    for dr in range(size):
        for dc in range(size):
            nr = x + dr
            nc = y + dc
            if paper[nr][nc] != init_V:
                flag = False
                break
        if not flag:
            break
    if flag:
        result[init_V] += 1
        return
    else:
        for i in range(3):
            for j in range(3):
                cut(x + (size//3) * i, y + (size//3) * j, size//3)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
result = [0] * 3
cut(0, 0, N)
print(result[-1])
print(result[0])
print(result[1])