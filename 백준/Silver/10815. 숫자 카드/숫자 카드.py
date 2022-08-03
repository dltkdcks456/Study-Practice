import sys
_, A, _, B = sys.stdin.read().rstrip().split('\n')
A = set(A.split())
B = list(B.split())
print(" ".join(map(lambda x: "1" if x in A else "0", B)))
