N, K = map(int, input().split())
num_li = list(range(1, N + 1))
step = 0
result = []
while num_li:
    step += K - 1
    step = step % len(num_li)
    result.append(num_li.pop(step))
print('<',end='')
print(*result,sep=', ',end = '')
print('>',end='')
