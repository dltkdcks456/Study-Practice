'''
가장 끝에서부터 확인하면서 들어온다.
cap의 용량만큼 배달과 수거를 병행한다.
2개의 리스트를 끝에서부터 보면서 빼는 것을 진행해보자
몫과 나머지가 떠오르긴 하지만 너무 복잡해서 단순하게 해결부터..
'''

def solution(cap, n, deliveries, pickups):
    answer = 0
    del_idx = pic_idx = n - 1
    
    def del_move():
        nonlocal del_idx
        while deliveries[del_idx] == 0:
            del_idx -= 1
            if del_idx == -1:
                break

    def pic_move():
        nonlocal pic_idx
        while pickups[pic_idx] == 0:
            pic_idx -= 1
            if pic_idx == -1:
                break

    while del_idx != -1 or pic_idx != -1:
        temp = cap
        if del_idx != -1:
            del_move()
        if pic_idx != -1:
            pic_move()

        if del_idx > pic_idx:
            answer += (del_idx + 1) * 2
        else:
            answer += (pic_idx + 1) * 2

        while temp > 0:
            temp -= 1
            if del_idx != -1:
                deliveries[del_idx] -= 1
            if pic_idx != -1:
                pickups[pic_idx] -= 1
            if del_idx != -1:
                del_move()
            if pic_idx != -1:
                pic_move()
    
    
    return answer