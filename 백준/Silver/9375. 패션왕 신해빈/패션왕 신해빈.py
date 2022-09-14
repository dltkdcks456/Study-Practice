T = int(input())
for _ in range(T):
    n = int(input())
    clothes = {}
    for _ in range(n):
        a, b = input().split()
        if b in clothes:
            clothes[b].append(a)
        else:
            clothes[b] = [a]
    s = 1
    for i in clothes.values():
        s *= len(i) + 1
    print(s - 1)