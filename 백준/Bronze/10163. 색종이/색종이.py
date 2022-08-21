N = int(input())
li = []
area = [[0] * 1001 for _ in range(1001)]
ans = []
for _ in range(N):
    li.extend(map(int, input().split()))
for i in range(N * 4 - 4, -1, -4):
    cnt = 0
    for r in range(li[i + 1], li[i + 1] + li[i + 3]):
        for c in range(li[i], li[i] + li[i + 2]):
            if area[r][c] == 0:
                area[r][c] = 1
                cnt += 1
    ans.append(cnt)
print(*ans[::-1], sep='\n')