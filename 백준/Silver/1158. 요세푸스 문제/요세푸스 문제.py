n, m = map(int, input().split())
num_list = [i for i in range(1, n + 1)]

i = m - 1
result = []

while num_list:
    if len(num_list) == 1:
        b = num_list.pop(0)
        result.append(b)
        break
    else:
        b = num_list.pop(i)
        result.append(b)
        i += m - 1
        if i >= len(num_list):
            i = i % len(num_list)

print('<', end = '')
print(*result, sep = ', ', end = '')
print('>', end = '')