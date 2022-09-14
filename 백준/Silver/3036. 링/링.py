def gcb(a, b):
    if b == 0:
        return a
    else:
        return gcb(b, a % b)


N = int(input())
li = list(map(int, input().split()))

for i in range(1, N):
    temp = gcb(li[0], li[i])
    print(f'{li[0]//temp}/{li[i]//temp}')