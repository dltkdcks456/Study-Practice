import sys
sys.setrecursionlimit(10 ** 9)

def dfs(start, end):
    if start > end:
        return
    temp = end + 1
    for i in range(start + 1, end + 1):
        if num[start] < num[i]:
            temp = i
            break

    dfs(start + 1, temp - 1)
    dfs(temp, end)
    print(num[start])


num = []
while True:
    try:
        text = int(input())
        num.append(text)
    except:
        break

dfs(0, len(num) - 1)