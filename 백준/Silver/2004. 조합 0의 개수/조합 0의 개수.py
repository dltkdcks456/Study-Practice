def find_2(n):
    m = n
    max_cnt = 0
    cnt = 0
    while n >= 1:
        n //= 2
        max_cnt += 1
    for i in range(1, max_cnt + 1):
        cnt += m // (2 ** i)
    return cnt

def find_5(n):
    m = n
    max_cnt = 0
    cnt = 0
    while n >= 1:
        n //= 5
        max_cnt += 1
    for i in range(1, max_cnt + 1):
        cnt += m // (5 ** i)
    return cnt

n, m = map(int, input().split())
a, b, c = n, n - m, m

cnt_2 = 0
cnt_5 = 0

cnt_2 += find_2(a)
cnt_5 += find_5(a)

cnt_2 -= find_2(b)
cnt_5 -= find_5(b)

cnt_2 -= find_2(c)
cnt_5 -= find_5(c)

print(min(cnt_2, cnt_5))