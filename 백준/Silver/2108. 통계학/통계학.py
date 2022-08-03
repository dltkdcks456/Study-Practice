import sys

N = int(sys.stdin.readline())
cnt_list = [0] * 8001
num_list = []
sum_total = 0

for i in range(N):
    n = int(sys.stdin.readline())
    cnt_list[n] += 1
    num_list.append(n)
    sum_total += n

num_list.sort()
max_cnt = max(set(cnt_list))
cnt_max_list = []

for j in range(-4000, 4001):
    if cnt_list[j]  == max_cnt:
        cnt_max_list.append(j)

if len(cnt_max_list) == 1:
    cnt_ans = cnt_max_list[0]
else:
    cnt_ans = sorted(cnt_max_list)[1]

avg_ans = round(sum_total/N)
mid_ans = num_list[N // 2]
range_ans = num_list[-1] - num_list[0]

print(avg_ans)
print(mid_ans)
print(cnt_ans)
print(range_ans)

