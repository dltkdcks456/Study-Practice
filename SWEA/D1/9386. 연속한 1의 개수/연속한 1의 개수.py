T = int(input())
for test in range(T):
    N = int(input())
    num_list = list(map(int, input())) + [0]
    cnt = 0
    maxV = 0
    for i in range(N + 1):
        if num_list[i] == 1:
            cnt += 1
        else:
            if cnt > maxV:
                maxV = cnt
                cnt = 0
    print(f'#{test + 1} {maxV}')
