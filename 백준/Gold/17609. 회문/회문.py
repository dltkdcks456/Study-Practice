import sys

def check1(text, left, right):
    global ans, flag
    start = left
    end = right
    while start < end:
        if text[start] != text[end]:
            ans = 2
            flag = False
            return 2
        start += 1
        end -= 1
    else:
        return 0

def check2(text, left, right):
    global ans
    start = left - 1
    last = right
    for k in range((right - left + 1) // 2):
        start += 1
        last -= 1
        if text[start] != text[last]:
            a = check1(text, start + 1, last)
            b = check1(text, start, last - 1)
            if a == 0 or b == 0:
                ans = 1
                return
            else:
                return


N = int(sys.stdin.readline())
for _ in range(N):
    text = sys.stdin.readline().rstrip()
    ans = 0
    flag = True
    check1(text, 0, len(text) - 1)
    if not flag:
        check2(text, 0, len(text))
    print(ans)