def pos(d, l):
    if d == 3:
        store_pos[l] = 1
        return l
    if d == 2:
        store_pos[l + c] = 1
        return l + c
    if d == 4:
        store_pos[- l + 2 * c + r] = 1
        return - l + 2 * c + r
    if d == 1:
        store_pos[- l + 2 * c + 2 * r] = 1
        return - l + 2 * c + 2 * r

def distance():
    global total
    for i in range(len(store_pos)):
        if i != X and store_pos[i] == 1:
            total += min(abs(X - i), abs(2 * (r + c) - abs(X - i)))

r, c = map(int, input().split())
N = int(input())
store_pos = [0] * 2 * (r + c) # 3, 2, 4, 1
for _ in range(N):
    d, l = map(int, input().split())
    pos(d, l)
se_d, se_l = map(int, input().split())
X = pos(se_d, se_l)
total = 0
distance()
print(total)