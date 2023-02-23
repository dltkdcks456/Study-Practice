'''
문제의 핵심은... DP와 다익스트라를 함께 써야하는 것
K개의 도로포장이 가능하기 때문에 포장된 개수의 상태와 함께 다익스트라를 진행한다.
똑똑한 사람들...
그리고 멍청한 나...ㅠㅠㅠ
'''
import sys
import heapq

def dijkstra():
    INF = 98765432109876543210
    q = []  
    visited = [[INF] * (N + 1) for _ in range(K + 1)]   # 2차원 형태의 거리를 넣을 리스트
    heapq.heappush(q, [0, 1, 0])    # 누적시간, 노드, 누적 K
    
    for i in range(K + 1):
        visited[i][1] = 0
    
    while q:
        sum_distance, node, curr_K = heapq.heappop(q)

        # 이미 최소의 거리가 정해졌다면 건너 뛴다.
        if visited[curr_K][node] < sum_distance:
            continue

        for x in adjList[node]:
            next_node, take_time = x


            # 포장하지 않고 지나가기
            if visited[curr_K][next_node] > visited[curr_K][node] + take_time:
                visited[curr_K][next_node] = visited[curr_K][node] + take_time
                heapq.heappush(q, [visited[curr_K][next_node], next_node, curr_K])

            # 포장하고 지나가기
            if curr_K < K and visited[curr_K + 1][next_node] > visited[curr_K][node]:
                visited[curr_K + 1][next_node] = visited[curr_K][node]
                heapq.heappush(q, [visited[curr_K + 1][next_node], next_node, curr_K + 1])

    ans = INF
    
    for l in visited:
        if ans > l[N]:
            ans = l[N]
    
    return ans

if __name__ == '__main__':
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    adjList = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b, T = map(int, input().split())
        adjList[a].append([b, T])
        adjList[b].append([a, T])
    
    result = dijkstra()

    print(result)