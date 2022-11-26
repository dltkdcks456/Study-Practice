import sys
input = sys.stdin.readline


N = int(input())
N_li = list(str(N))
N_length = len(N_li)
M = int(input())
num = list(range(0, 10))
try:
    li = list(map(int, input().split()))
    for i in li:
        num.remove(i)
except:
    pass

minV = abs(N - 100)
# print(num)
if M == 9 and num == [0]:
    diff_0 = abs(N) + 1
    if diff_0 < minV:
        minV = diff_0
elif M != 10:
    if 1 in num:    # 1이 포함되어 있는 경우 자리 수가 하나 더 큰 것을 비교해줘야한다.
        # 한 자리수 큰 경우
        up = int('1' + str(min(num)) * N_length)
        diff_up = abs(N - up) + N_length + 1
        if diff_up < minV:
            minV = diff_up

        # 한 자리수 낮은 경우
    if N_length >= 2:
        down = int(str(max(num)) * (N_length - 1))
        diff_down = abs(N - down) + (N_length - 1)
        if diff_down < minV:
            minV = diff_down

    # 같은 자리수인 경우
    # 숫자가 같은 것이 있으면 그대로 넣고 없을 경우 해당 숫자보다 바로 한 단계 큰 숫자와 한 단계 작은 숫자를 넣어준다
    # 한 단계 높은 숫자를 넣을 경우 그 뒤의 자리수에는 최솟값만 들어오고
    # 한 단계 낮은 경우에는 그 반대이다.

    N_li_upside = sorted(num)
    N_li_downside = sorted(num, reverse= True)
    max_num = min_num = 0

    result_up = []
    result_down = []

    cnt = N_length
    flag = False
    for j in N_li:
        cnt -= 1
        j = int(j)
        if j in num:
            result_up.append(j)
            result_down.append(j)
        else:
            for k in N_li_upside:
                k = int(k)
                if k > j:
                    result_up.append(k)
                    for _ in range(cnt):
                        result_up.append(min(num))
                    flag = True
                    break
            for l in N_li_downside:
                l = int(l)
                if l < j:
                    result_down.append(l)
                    for _ in range(cnt):
                        result_down.append(max(num))
                    flag = True
                    break
            if flag:
                break
    if flag:
        if len(result_up) == N_length:
            num_up = int(''.join(map(str, result_up)))
            diff_up = abs(N - num_up) + N_length
            if diff_up < minV:
                minV = diff_up
        if len(result_down) == N_length:
            num_down = int(''.join(map(str, result_down)))
            diff_down = abs(N - num_down) + N_length
            if diff_down < minV:
                minV = diff_down
    else:
        diff_same = N_length
        if diff_same < minV:
            minV = diff_same

    result_UP = []
    result_DOWN = []
    first = int(N_li[0])
    CNT = N_length - 1
    flag2 = False
    for m in N_li_upside:
        m = int(m)
        if m > first:
            result_UP.append(m)
            for _ in range(CNT):
                result_UP.append(min(num))
                flag2= True
            break
    for n in N_li_downside:
        n = int(n)
        if n < first:
            result_DOWN.append(n)
            for _ in range(CNT):
                result_DOWN.append(max(num))
                flag2= True
            break
    if result_UP:
        num_UP = int(''.join(map(str, result_UP)))
        if num_UP != 0:
            diff_UP = abs(N - num_UP) + N_length
            if diff_UP < minV:
                minV = diff_UP
    if result_DOWN:
        num_DOWN = int(''.join(map(str, result_DOWN)))
        if num_DOWN != 0:
            diff_DOWN = abs(N - num_DOWN) + N_length
            if diff_DOWN < minV:
                minV = diff_DOWN
print(minV)