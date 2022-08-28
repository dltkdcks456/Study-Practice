import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
li_sort = sorted(set(li))
li_dict = {j : 0 for j in li}
cnt_li = [0] * len(li_sort)
for i in range(1, len(li_sort)):
    if li_sort[i] > li_sort[i - 1]:
        cnt_li[i] = cnt_li[i - 1] + 1
        li_dict[li_sort[i]] = cnt_li[i]
    else:
        cnt_li[i] = cnt_li[i - 1]
for j in li:
    print(li_dict[j], end = ' ')