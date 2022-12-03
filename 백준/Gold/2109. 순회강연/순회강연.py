import sys
import heapq
input = sys.stdin.readline

'''
강연료가 가장 큰 값부터 진행(최대 힙 활용)
데드라인 이내의 빈 자리에 강연 진행
강연을 진행 했을 때 해당 날 수를 기억(last_idx) 
-> 그 앞의 날짜들 중에서도 last_idx보다 큰 값들을 last_idx로 바꿔준다(어차피 다 강연을 했기 때문에 순회 불필요) 
'''

n = int(input()) # 대학 개수
# 데드라인마다 강연을 할 수 있는 빈 공간들을 표시, 초기에는 모두 강연이 비어 있으므로 데드라인만큼 빈 공간이 있다.
last_idx = [i for i in range(10001)]
visited = [0] * 10001
lecture = []
for _ in range(n):
    p, d = map(int, input().split())  # p: 강연료, d: 데드 라인
    heapq.heappush(lecture, [-p, d])  # 강연료를 기준으로 최대힙 진행
# print(lecture)
sumV = 0    # 강연료 누적합
while lecture:
    next_lecture = heapq.heappop(lecture)
    next_lecture[0] = -next_lecture[0]
    money, deadline = next_lecture[0], next_lecture[1]
    for day in range(deadline, 0, -1):  # 해당 강의가 갈 수 있는 범위부터 시작
        if visited[day] == 0:
            visited[day] = 1    # 방문기록
            sumV += money   # 강연료 받기
            last_idx[deadline] = day - 1 # 현재 방문 날의 이전부터 강연 가능(갱신)
            for check in range(deadline - 1, 0, -1):    # 그 앞의 데드라인들이 갈 수 있는 시간을 갱신
                if last_idx[check] > day - 1:
                    last_idx[check] = day - 1
            break
# print(visited)
# print(last_idx)
print(sumV)