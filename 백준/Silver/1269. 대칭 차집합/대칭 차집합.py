import sys
N, M = map(int, sys.stdin.readline().split())
n_set = set(map(int, sys.stdin.readline().split()))
m_set = set(map(int, sys.stdin.readline().split()))
print(len(n_set - m_set) + len(m_set - n_set))
