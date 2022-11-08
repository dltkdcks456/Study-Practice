import sys
input = sys.stdin.readline

def like_check(li):
    for l in range(1, M + 1):
        x, y, z = log[l]
        if frog_like[li[x]][z] != frog_like[li[y]][z]:
            return False
    return True

def check(n, m): # 연꽃 위치, 개구리 번호, 좋아하는 것, 점수
    global flag
    if flag:
        return
    if n == m:
        ck = like_check(result)
        if ck:
            flag = True
            print('YES')
            print(*result[1:])
        return
    else:
        for k in leaf[n]:
            if k not in result:
                result[n] = k
                check(n + 1, m)
                result[n] = 0
            if flag:
                return

N, M = map(int, input().split())
frog_like = [[]]  # 개구리 각각의 흥미도
for _ in range(N):
    frog_like.append([0] + list(map(int, input().split())))
leaf = [[] for _ in range(N + 1)]   # 개구리의 연꽃 선호도
for i in range(1, N + 1):
    a, b = map(int, input().split())
    if a == b:
        leaf[a].append(i)
    else:
        leaf[a].append(i)
        leaf[b].append(i)
log = [[]]
for _ in range(M):
    A, B, T = map(int, input().split())
    log.append([A, B, T])

result = [0] * (N + 1)
flag = False
check(1, N + 1)

if not flag:
    print('NO')