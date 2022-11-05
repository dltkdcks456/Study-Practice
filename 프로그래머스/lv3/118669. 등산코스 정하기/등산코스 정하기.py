from collections import deque
import heapq
'''
출입구마다 함수 실행을 통해 산봉우리까지의 intensity 갱신 진행
visited를 활용해서 방문기록 남기기
가는 길마다 가중치를 비교해서 max값만 들고 지나가기
단, 산봉우리에서는 그 가중치들 중에서 min값을 기록한다.
다시 돌아오는 길은 같은 루트로 돌아오면 되기 때문에 다시 구할 필요는 없다.
'''

def solution(n, paths, gates, summits):
    adjList = [[] for _ in range(n + 1)]
    gate_dict = set(gates)
    summits_dict = set(summits)

    for i in paths:
        v, u, w = i
        adjList[v].append([u, w])
        adjList[u].append([v, w])

    answer = 100000000
    peak = n + 1
    total_minV = 100000000
    visited = [100000000] * (n + 1)
    for z in gates:
        q = []
        heapq.heappush(q, [0, z])
        while q:
            maxV, x = heapq.heappop(q)
            if maxV > total_minV:
                continue
            for n_x, n_maxV in adjList[x]:
                temp_maxV = maxV
                if n_x in gate_dict:
                    continue
                if n_maxV > temp_maxV:
                    temp_maxV = n_maxV  # intensity 갱신
                if n_x in summits_dict:  # 봉우리일 경우
                    if visited[n_x] > temp_maxV:  # 가장 작은 값으로 계속 갱신
                        visited[n_x] = temp_maxV
                        if total_minV > temp_maxV:
                            total_minV = temp_maxV
                            peak = n_x
                        elif total_minV == temp_maxV and peak > n_x:
                            peak = n_x
                else:
                    if visited[n_x] > temp_maxV and temp_maxV <= total_minV:
                        visited[n_x] = temp_maxV
                        heapq.heappush(q, [temp_maxV, n_x])


    result = [peak, total_minV]

    return result