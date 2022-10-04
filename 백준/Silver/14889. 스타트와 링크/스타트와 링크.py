import sys

def comb(n, m, j):
    global minV
    if n == m:
        if tuple(chosen) not in group:
            group.add(tuple(chosen[:]))
            rest_team = []
            for k in range(1, N + 1):
                if k not in chosen:
                    rest_team.append(k)
            s1 = s2 = 0
            for m in range(N//2 - 1):
                for n in range(m + 1, N//2):
                    s1 += synergy[chosen[m]][chosen[n]] + synergy[chosen[n]][chosen[m]]
                    s2 += synergy[rest_team[m]][rest_team[n]] + synergy[rest_team[n]][rest_team[m]]
            diff = abs(s1 - s2)
            if diff < minV:
                minV = diff
        return
    else:
        for i in range(j, N):
            if visited[i] == 0:
                visited[i] = 1
                chosen[n] = team[i]
                comb(n + 1, m, i + 1)
                visited[i] = 0

N = int(input())
team = list(range(1, N + 1))
synergy = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
chosen = [0] * (N//2)
visited = [0] * N
group = set()
minV = 2000
comb(0, N//2, 0)
print(minV)