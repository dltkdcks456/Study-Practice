import sys
T = int(sys.stdin.readline())
for i in range(T):
    li = sys.stdin.readline().rstrip()
    ans = 0
    for j in li:
        if j == '(':
            ans += 1
        else:
            ans -= 1
        if ans < 0:
            ans = 1
            break
    if ans == 0:
        print('YES')
    else:
        print('NO')