'''
누적합 형태로 진행하면 될 듯하다
투 포인터로 갑시다
'''
def solution(queue1, queue2):
    answer = -2
    total_queue = queue1 + queue2
    point1 = point2 = -1
    total_sumV = (sum(queue1) + sum(queue2))
    
    if total_sumV % 2:
        return -1
    
    goal_sumV = total_sumV // 2
    sumV = 0
    minV = 2147000
    signal = False
    # print(goal_sumV)
    
    while point1 != len(total_queue) - 1:
        if sumV == goal_sumV:
            # print('유후', point1, point2)
            signal = True
            if point2 + 1 <= len(queue1):
                if point2 + 1 == len(queue1):
                    move_cnt = point1 + 1
                else:
                    move_cnt = point1 + 1 + len(queue1) + point2 + 1
            else:
                move_cnt = point1 + (point2 + 1 - len(queue1)) + 1
            
            if move_cnt < minV:
                minV = move_cnt
            
            if point2 < len(total_queue) - 1:
                point2 += 1
                sumV += total_queue[point2]
            else:
                point1 += 1
                sumV -= total_queue[point1]
            
        elif sumV < goal_sumV:
            if point2 < len(total_queue) - 1:
                point2 += 1
                sumV += total_queue[point2]
            else:
                if signal:
                    answer = minV
                    break
                else:
                    return -1
            
        elif sumV > goal_sumV:
            point1 += 1
            sumV -= total_queue[point1]
            
    answer = minV
    # print(minV)
    
    if answer == 2147000:
        return -1

    
    return answer