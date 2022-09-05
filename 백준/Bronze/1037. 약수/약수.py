N = int(input())
li = list(map(int,input().split()))
if N == 1:
    print(li[0] ** 2)
else:
    print(min(li) * max(li))