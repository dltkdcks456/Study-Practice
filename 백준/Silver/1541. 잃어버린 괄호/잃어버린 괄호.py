import sys

data = list(input().split('-'))
if len(data) != 1:
    for i in range(len(data)):
        if data[i].isdigit():
            data[i] = int(data[i])
        else:
            data[i] = sum(map(int, data[i].split('+')))
else:
    for i in range(len(data)):
        if data[i].isdigit():
            data[i] = int(data[i])
        else:
            data[i] = sum(map(int, data[i].split('+')))

ans = data[0]
for j in range(1, len(data)):
    ans -= data[j]
print(ans)