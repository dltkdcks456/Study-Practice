import sys
import heapq
input = sys.stdin.readline

def find_set(x):                            # 대표값을 찾는 함수
    while rep[x] != x:                      # 자기 자신을 가리키는 곳이 대표값
        x = rep[x]
    return x

def union_set(a, b):                        # 집합을 합치는 함수
    rep[find_set(b)] = find_set(a)          #  b의 대표값을 a의 대표값으로 변경

V, E = map(int, input().split())
data = []                                   # 입력값 저장 리스트
rep = [i for i in range(V + 1)]             # 대표원소 저장 리스트
for _ in range(E):
    u, v, w = map(int, input().split())
    heapq.heappush(data, [w, u, v])

s = 0                                       # 합을 구할 변수
for j in range(E):                          # 순환 트리가 아니면서 최솟값을 계속 더해가기
    w, u, v = heapq.heappop(data)
    if find_set(u) != find_set(v):
        s += w
        union_set(u, v)
print(s)