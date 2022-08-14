import sys

N, M = map(int, sys.stdin.readline().split())
po = {sys.stdin.readline().rstrip() : i + 1 for i in range(N)}
po_rev = {v: k for k, v in po.items()}
for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if question.isalpha():
        print(po[question])
    else:
        print(po_rev[int(question)])