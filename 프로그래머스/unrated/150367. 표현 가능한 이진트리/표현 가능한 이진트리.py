'''
전위 순회로 읽은 값을 완전 이진트리에 삽입
이진 트리를 하나씩 탐색하면서 자식 중에 1이 있지만 부모가 0인 녀석이 있으면 이진트리를 만들 수 없으므로 0을 출력
그 외에는 1 출력
'''
def solution(numbers):
    answer = []
    
    # 이진수로 만들기
    def binary(num):
        temp = ''
        quotient = num // 2
        rest = num % 2
        if quotient != 0:
            temp = str(rest) + temp
            return binary(quotient) + temp
        else:
            return str(rest)
    
    def limit(x):
        # n은 이진 트리 높이를 의미, max_number는 이진 트리를 가득 채웠을 때 들어갈 수 있는 최댓값
        n = 1
        while True:
            max_number = 2 ** ((2 ** n) - 1)
            if max_number <= x:
                n += 1
            else:
                break
        return n
    
    # 전위 순회
    def pre_order(y):
        nonlocal idx
        if y < len(binary_tree):
            pre_order(2 * y)
            binary_tree[y] = int(binary_number[idx])
            idx += 1
            pre_order(2 * y + 1)
    
    # 이진 트리 생성 가능 여부 확인
    def check_binary_tree(N):
        nonlocal temp
        if 2 * N + 1 < len(binary_tree):
            if (binary_tree[2 * N] == 1 or binary_tree[2 * N + 1] == 1) and binary_tree[N] == 0:
                temp = 0
            check_binary_tree(2 * N)
            check_binary_tree(2 * N  + 1)
    
    for number in numbers:
        # 이진수
        binary_number = binary(number)
        # 이진 트리 높이
        level = limit(number)
        # 이진 트리 공간
        binary_tree = [0] * (2 ** level)
        
        if len(binary_number) < len(binary_tree) - 1:
            binary_number = '0' * (len(binary_tree) - 1 - len(binary_number)) +binary_number
        # print('높이', level)
        # print('이진수', binary_number)
        idx = 0
        pre_order(1)
        # print('이진 트리', binary_tree)
        # print('이진 트리 길이', len(binary_tree))
        
        temp = 1
        check_binary_tree(1)
        # print(temp)
        answer.append(temp)
        
    return answer