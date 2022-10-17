import sys
input = sys.stdin.readline

def comb(q, p, li):
    if q == p:
        data = '+'.join(map(str, chosen))
        bruteforce.append(data)
        return
    else:
        for x in range(1, 4):
            if li[x] > 0:
                li[x] -= 1
                chosen[q] = x
                comb(q + 1, p, li)
                li[x] += 1

n, k = map(int, input().split())
case = []
for i in range(n // 3 + 1):
    for j in range(n // 2 + 1):
        temp = 3 * i + 2 * j
        if temp <= n:
            case.append([0, n - temp, j, i])
bruteforce = []
for l in case:
    sumV = sum(l)
    chosen = [-1] * (sumV)
    comb(0, sumV, l)
if k - 1 >= len(bruteforce):
    print(-1)
else:
    print(sorted(bruteforce)[k - 1])