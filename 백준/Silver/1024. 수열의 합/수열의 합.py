N, L = map(int, input().split())
n_sum = 0
start = 0
diff = 0

for i in range(L, 101):       # 리스트 개수
    for j in range(N // i - i, N // i + 1):  # 시작점
        n_sum = 0
        if j >= 0:
            for k in range(i):      # 시작점부터 연속된 합
                n_sum += j + k
            if n_sum == N:
                start = j
                diff = i
                break
        else:
            continue
    if n_sum == N:
        break

result = [l + start for l in range(diff)]    

if result:
    print(*result)
else:
    print(-1)