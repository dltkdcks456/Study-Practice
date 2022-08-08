N, M = map(int,input().split())
matrix1 = [list(map(int,input().split())) for i in range(N)]

M, K = map(int,input().split())
matrix2 = [list(map(int,input().split())) for j in range(M)]

for n in range(N):
    for k in range(K):
        sum_n = 0
        for m in range(M):
            pro_n = matrix1[n][m] * matrix2[m][k]
            sum_n += pro_n
        print(sum_n, end= ' ')
    print()
    