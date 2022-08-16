N = int(input())
li = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.insert(li[i], i + 1)
print(' '.join(map(str, ans[::-1])))