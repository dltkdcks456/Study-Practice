'''
제일 윗 줄부터 아래로 내려오면서 퀸을 두고, 
해당 줄의 퀸은 위에 분포하는 퀸을 확인하면서 백트래킹을 진행하자.
'''

def solution(n):
    def NQueen(row, K):
        nonlocal answer
        # 그 위쪽 체스판에서 퀸 배열을 확인하기
        if row == n:
            if K == n:
                answer += 1
            else:
                return

        for c in range(n):
            if column_Queen[c] != 1:
                for delta_row in range(1, row + 1):
                    if c - delta_row >= 0 and board[row - delta_row][c - delta_row] == 1:
                        break
                    elif board[row - delta_row][c] == 1:
                        break
                    elif c + delta_row < n and board[row - delta_row][c + delta_row] == 1:
                        break
                else:
                    column_Queen[c] = 1
                    board[row][c] = 1
                    NQueen(row + 1, K + 1)
                    column_Queen[c] = 0
                    board[row][c] = 0

    board = [[0] * n for _ in range(n)]
    column_Queen = [0] * n
    answer = 0

    for col in range(n):
        board[0][col] = 1
        column_Queen[col] = 1
        NQueen(1, 1)
        board[0][col] = 0
        column_Queen[col] = 0
    
    return answer