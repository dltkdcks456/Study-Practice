for test in range(10):
    tc = int(input())
    num_list = [list(map(int, input().split())) for i in range(100)]

    max_ans = 0
    for i in range(100):
        s_r = 0
        s_c = 0
        s_cross_r = 0
        s_cross_l = 0
        for j in range(100):
            s_r += num_list[i][j]
            s_c += num_list[j][i]
            if i == j:
                s_cross_r += num_list[i][j]
            if i + j == 100:
                s_cross_l += num_list[i][j]
        if max_ans < s_r:
            max_ans = s_r
        if max_ans < s_c:
            max_ans = s_c
        if max_ans < s_cross_r:
            max_ans = s_cross_r
        if max_ans < s_cross_l:
            max_ans = s_cross_l
    print(f'#{test + 1} {max_ans}')