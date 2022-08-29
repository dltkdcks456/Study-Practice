def fac(n):
    if n <= 1:
        return 1
    else:
        return fac(n - 1) * n

T = int(input())
for test in range(T):
    N = int(input())
    cnt = 0
    for i in range(N//3 + 1):
        for j in range(N//2 + 1):
            if 3 * i + 2 * j <= N:
                k = N - (3 * i + 2 * j)
                cnt += fac(i + j + k)//fac(i)//fac(j)//fac(k)
    print(cnt)