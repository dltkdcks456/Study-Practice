import sys

N, M = map(int, input().split())
poketmon_dict = {sys.stdin.readline().rstrip() : i + 1 for i in range(N)}
poketmon_dict_rev = {v: k for k, v in poketmon_dict.items()}
for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if question.isalpha():
        print(poketmon_dict[question])
    else:
        print(poketmon_dict_rev[int(question)])