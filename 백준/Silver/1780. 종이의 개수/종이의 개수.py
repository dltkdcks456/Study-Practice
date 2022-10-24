import sys

def cut(x, y, size):
    init_V = paper[x][y]
    for dr in range(size):
        check = set(paper[x + dr][y: y + size])
        if len(check) >= 2 or init_V not in check:
            new_size = size // 3
            for i in range(3):
                for j in range(3):
                    cut(x + new_size * i, y + new_size * j, new_size)
            return
    result[init_V] += 1
    return


N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
result = [0] * 3
cut(0, 0, N)
print(result[-1])
print(result[0])
print(result[1])