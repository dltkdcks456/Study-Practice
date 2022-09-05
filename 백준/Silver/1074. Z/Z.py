N, r, c = map(int, input().split())

ans = 0
while N != 1:
    if r // (2 ** (N - 1)):
        ans += 2 ** (2 * N) // 2
        r -= 2 ** (N - 1)
    if c // (2 ** (N - 1)):
        ans += 2 ** (2 * N) // 4
        c -= 2 ** (N - 1)
    N -= 1
if r == 0 and c == 1:
    ans += 1
elif r == 1 and c == 0:
    ans += 2
elif r == 1 and c == 1:
    ans += 3

print(ans)