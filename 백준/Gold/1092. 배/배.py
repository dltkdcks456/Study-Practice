import sys

input = sys.stdin.readline
N = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
load = sorted((map(int, input().split())))
cnt = 0
while load:
    flag = True
    for i in range(len(crane)):
        if load:
            limit = crane[i]
            start = 0
            end = len(load) - 1
            while start <= end:
                mid = (start + end) // 2
                if load[mid] == limit:
                    flag = False
                    load.pop(mid)
                    break
                elif load[mid] > limit:
                    end = mid - 1
                elif load[mid] < limit:
                    start = mid + 1
            else:
                if load[end] > limit:
                    break
                flag = False
                load.pop(end)
        else:
            break
    cnt += 1
    if flag:
        cnt = -1
        break
print(cnt)