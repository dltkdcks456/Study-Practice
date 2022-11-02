import sys
input = sys.stdin.readline

def bin(x):
    global cnt
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if num[mid] > x:
            r = mid - 1
        elif num[mid] < x:
            l = mid + 1
        else:
            if x in group and (X - x) in group:
                return
            else:
                cnt += 1
                return


n = int(input())
num = sorted(list(map(int, input().split())))
X = int(input())
cnt = 0
group = set()
for i in num:
    k = X - i
    if k > 0:
        bin(k)
    else:
        break
print(cnt//2)