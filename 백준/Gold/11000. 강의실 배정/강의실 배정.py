import sys
import heapq


N = int(sys.stdin.readline())
time = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
heap = []

for i in range(len(time)):
    ns, ne = time[i]
    if i != 0:
        if heap[0] <= ns:
            heapq.heappushpop(heap, ne)
        else:
            heapq.heappush(heap, ne)
    else:
        heapq.heappush(heap, time[0][1])

print(len(heap))