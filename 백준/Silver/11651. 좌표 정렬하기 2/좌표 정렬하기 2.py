N = int(input())
pos_list = []
for i in range(N):
    x, y = map(int, input().split())
    pos_list.append((y, x))
b = sorted(pos_list)
for j in b:
    print(j[-1], j[0])