N = int(input())
student = [list(map(int, input().split())) for i in range(N)]

for m in student:
    cnt = 0
    for n in student:
        if m[0] < n[0] and m[1] < n[1]:
            cnt += 1
    print(cnt + 1, end = ' ')
