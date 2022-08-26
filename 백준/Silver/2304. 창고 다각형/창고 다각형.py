import sys

def find_max():
    global maxV
    maxV = max(L)
    for i in range(len(L)):
        if L[i] == maxV:
            maxV_pos.append(i)
            break
    for j in range(len(L) - 1, 0, -1):
        if L[j] == maxV:
            maxV_pos.append(j)
            break

def puls_building(start, end):
    global total
    for M_M in range(maxV_pos[0], maxV_pos[1] + 1):
        total += maxV
    jump_s = L[start]
    for s_M in range(start, maxV_pos[0]):
        if L[s_M] > jump_s:
            jump_s = L[s_M]
        total += jump_s
    jump_e = L[end]
    for e_M in range(end, maxV_pos[1], -1):
        if L[e_M] > jump_e:
            jump_e = L[e_M]
        total += jump_e


N = int(sys.stdin.readline())
L = [0] * 1001
start = 1001
end = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())

    L[a] = b
    if a < start:
        start = a
    if a > end:
        end = a
total = 0
maxV_pos = []
find_max()
puls_building(start, end)
print(total)