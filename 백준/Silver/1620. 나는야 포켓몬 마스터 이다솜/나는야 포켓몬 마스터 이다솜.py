import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
po_li = [0] + [sys.stdin.readline().rstrip() for _ in range(N)]
po_dict = dict(zip(po_li, range(N + 1)))
ans = [po_li[int(t)] if (t:= sys.stdin.readline().rstrip()).isdigit() else str(po_dict[t])  for _ in range(M)]
print('\n'.join(ans))