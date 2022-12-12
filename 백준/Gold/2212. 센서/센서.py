import sys
import heapq
input = sys.stdin.readline

'''
[답지 활용]
나열된 수를 k개로 나누어주는 것을 생각할 때는 서로 간의 연결을 끊어주는 것으로
그 분할된 집합을 만들어낼 수 있다.
1 3 6 6 7 9
5개의 연결고리가 있고 하나만 끊어준다면 2개의 분할된 구역으로 나눠지므로
그 연결고리가 긴 녀석들만 지워주면 된다.
'''

N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))
if K <= N:
    diff = []
    for i in range(1, N):
        heapq.heappush(diff, -(arr[i] - arr[i - 1]))
    for _ in range(K - 1):
        heapq.heappop(diff)
    print(-sum(diff))
else:
    print(0)