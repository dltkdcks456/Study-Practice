def cnt(A_n, B_n, A_li, B_li):            # A, B의 개수와 각각의 도형들이 적혀있는 리스트 입력
    A_list = [0] * 5                        # A, B를 탐색하며 해당 도형의 숫자를 센다
    B_list = [0] * 5
    
    for i in A_li:
        A_list[i] += 1
    for j in B_li:
        B_list[j] += 1
    return A_list, B_list

def comp(A_list, B_list):                   # 도형의 개수 비교 진행(s: 별, o:동그라미, r:사각형, t:세모)
    for idx in range(4, 0, -1):             # 각 도형일 때의 승리 조건
        if A_list[idx] > B_list[idx]:
            return 'A'
        elif B_list[idx] > A_list[idx]:
            return 'B'
        else:                               # 무승부일 경우 다음 도형으로 이동
            continue
    return 'D'

T = int(input())
for i in range(T):
    A_total = list(map(int, input().split()))
    B_total = list(map(int, input().split()))
    A_n, A_li = A_total[0], A_total[1:]
    B_n, B_li = B_total[0], B_total[1:]

    A_list, B_list = cnt(A_n, B_n, A_li, B_li)
    print(comp(A_list, B_list))