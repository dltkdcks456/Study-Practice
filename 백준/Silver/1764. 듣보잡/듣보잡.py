N, M = map(int, input().split())
set1 = {input() for _ in range(N)}
set2 = {input() for _ in range(M)}
result = sorted(list(set1 & set2))
print(len(result))
for i in result:
    print(i)