T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    up_prod = 1
    down_prod = 1
    up_num = [up_prod * i for i in range(M, M - N, -1)]
    down_num = [j for j in range(1, N + 1)]

    for i in up_num:
        up_prod *= i
    for j in down_num:
        down_prod *= j
 
    print(int(up_prod / down_prod))