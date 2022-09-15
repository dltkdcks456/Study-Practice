import sys
from heapq import *

input=sys.stdin.readline



N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x:
        heappush(heap, -x)
    else:
        print(-heappop(heap) if heap else 0)