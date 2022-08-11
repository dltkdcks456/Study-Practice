N = int(input())
text = [input() for _ in range(N)]
len_text = sorted(set([len(i) for i in text]))
ans = []
for i in len_text:
    arr = []
    for j in text:
        if len(j) == i and j not in arr:
            arr.append(j)
    arr = sorted(arr)
    for k in arr:
        ans.append(k)
print('\n'.join(ans))