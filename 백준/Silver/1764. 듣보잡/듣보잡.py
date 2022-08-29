import sys

N, M = map(int, sys.stdin.readline().split())
set1 = {sys.stdin.readline().rstrip() for _ in range(N)}
set2 = {sys.stdin.readline().rstrip() for _ in range(M)}
result = sorted(list(set1 & set2))
print(len(result))
for i in result:
    print(i)