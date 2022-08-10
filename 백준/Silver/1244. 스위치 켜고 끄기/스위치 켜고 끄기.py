def boy(boy_pos, switch, N):                            # boy_pos: 남학생의 위치, switch: 스위치 리스트, N: 스위치의 총 개수
    for i in range(N):
        if (i + 1) % boy_pos:                           # 배수에 대하여 스위치를 바꿔줌
            continue
        else:
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0

def girl(girl_pos, switch, N):                          # girl_pos: 여학생의 위치, switch: 스위치 리스트, N: 스위치의 총 개수
    if girl_pos == 1 or girl_pos == N:                  # 양 끝에 위치한 경우
        if switch[girl_pos - 1] == 0:
            switch[girl_pos - 1] = 1
        else:
            switch[girl_pos - 1] = 0
    else:                                               # 내부에 존재하는 경우
        diff = min(girl_pos - 1, N - girl_pos)
        for j in range(diff + 1):
            if switch[girl_pos - 1 - j] == switch[girl_pos - 1 + j]:
                if switch[girl_pos - 1 - j] == 0:
                    switch[girl_pos - 1 - j] = switch[girl_pos - 1 + j] = 1
                else:
                    switch[girl_pos - 1 - j] = switch[girl_pos - 1 + j] = 0
            else:
                break

def gender(gender, pos):
    if gender == 1:
        boy(pos, switch, N)
    else:
        girl(pos, switch, N)


N = int(input())
switch = list(map(int, input().split()))
students = int(input())
for k in range(students):
    gender_, pos = map(int, input().split())
    gender(gender_, pos)

for i in range(N):
    if (i + 1) % 20:
        print(switch[i], end = ' ')
    else:
        print(switch[i], end = ' ')
        print()