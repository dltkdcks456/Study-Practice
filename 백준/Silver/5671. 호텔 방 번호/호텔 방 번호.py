import sys
while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
        cnt = 0

        def sol(x):
            num_list = [0] * 10
            global cnt
            for i in list(map(int,str(x))):
                if num_list[i] == True:
                    cnt = cnt + 1
                    break
                else:
                    num_list[i] = True

        for j in range(N, M + 1):
            sol(j)
        print((M - N + 1) - cnt)
    except:
        break