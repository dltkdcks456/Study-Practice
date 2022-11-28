M = int(input())
N = int(input())
m = int(M ** 0.5)
sumV = 0
minV = 0
for i in range(m, int(100000 ** 0.5) + 1 ):
    if N >= i ** 2 >= M:
        sumV += i ** 2
        if not minV:
            minV = i ** 2
if minV != 0:
    print(sumV)
    print(minV)
else:
    print(-1)
