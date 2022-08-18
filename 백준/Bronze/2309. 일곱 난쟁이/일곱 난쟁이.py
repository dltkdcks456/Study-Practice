N = 9
people = [int(input()) for _ in range(N)]
subset = []
for i in range(1<<9):
    li = []
    for j in range(9):
        if i & (1<<j):
            li.append(people[j])
    if len(li) == 7:
        subset.append(li)

for k in subset:
    if sum(k) == 100:
        print(*sorted(k), sep = '\n')
        break
