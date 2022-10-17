import sys
from collections import deque
input = sys.stdin.readline

# 문제 조건
# 아기상어는 초기에 2의 크기를 가지고 상하좌우로 움직인다. 이동 시에도 자기 자신보다 크기가 큰 물고기는 먹을 수 없다.
# 자기 자신보다 큰 물고기는 먹을 수 없으며, 자신의 크기만큼 물고기를 먹으면 크기가 1 증가한다.
# 먹을 수 있는 물고기는 가장 가까운 거리부터 먹으며, 여러 마리일 경우 가장 위쪽, 그리고 가장 왼쪽 물고기를 먹는다

# 필요 조건
# visited를 계속 갱신하면서 가장 가까운 물고기 탐색 진행(시간 복잡도가 높아질 염려)
# bfs를 통해 물고기를 탐색한다.(함수 내부에 물고리를 저장할 리스트도 마련)
# 물고기를 먹으면 먹은 개수를 카운트해줄 변수와 상어의 크기를 한번 더 확인해줌

def bfs(pos):
    global shark_size, total_time, eat, mom_fish, shark_pos
    catch = True                                    # 물고기를 발견했을 시의 신호
    time = 1000000000
    q = deque([pos])
    visited = [[0] * N for _ in range(N)]           # 방문기록
    visited[pos[0]][pos[1]] = 1                     # 초기 값은 1
    fish_pos = []                                   # 물고기의 위치 저장
    while q:
        r, c = q.popleft()
        for d in range(4):                          # 우, 하, 좌, 상에 대해 탐색 진행
            nr = r + dr[d]
            nc = c + dc[d]
            # sea의 범위를 넘어가지 않으면서 물고기의 크기가 작은 곳만 이동
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0 and sea[nr][nc] <= shark_size:
                if sea[nr][nc] == shark_size or sea[nr][nc] == 0 and catch:                # 만약 물고기가 없으면 그냥 진행
                    visited[nr][nc] = visited[r][c] + 1
                    q.append([nr, nc])
                elif 0 < sea[nr][nc] < shark_size:                               # 물고기가 있으면 물고기의 위치를 기록하고, 물고기 발견 신호를 ON
                    visited[nr][nc] = visited[r][c] + 1
                    fish_pos.append([nr, nc, visited[nr][nc]])
                    if time > visited[r][c]:
                        time = visited[r][c]

                    catch = False


    if fish_pos:
        fish_pos.sort(key=lambda z: (z[2], z[0], z[1]))                                   # r좌표에 대해 오름차순, c좌표에 대한 오름차순 진행
        # print(fish_pos)
        sea[fish_pos[0][0]][fish_pos[0][1]] = 0                                     # 물고기 잡아 먹은 곳은 0으로 변경
        shark_pos = [fish_pos[0][0], fish_pos[0][1]]
        eat += 1                                                                    # 한 마리 먹었으니 추가 해줌
        total_time += time                                                          # 먹는데까지의 시간 기록
        # print(f'total_time: {total_time}')
        # print(f'tiem:{time}')
        # for i in visited:
        #     print(i)
        # print()
        # for j in sea:
        #     print(j)
        if eat == shark_size:                                                       # 크기만큼 먹었을 경우 상어 크기 증가
            shark_size += 1
            eat = 0
    else:
        mom_fish = False
        return


N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
shark_pos = []
shark_size = 2
total_time = 0
eat = 0

for x in range(N):
    flag = True                                     # 상어를 찾게 되면 종료해줄 신호
    for y in range(N):
        if sea[x][y] == 9:                          # 상어의 위치를 찾으면 저장
            flag = False
            shark_pos.extend([x, y])
            sea[x][y] = 0
            break
    if not flag:
        break

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

mom_fish = True
while mom_fish:
    bfs(shark_pos)
print(total_time)