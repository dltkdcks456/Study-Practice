'''
셀 하나에는 [value, [병합된 위치들]]
'''

def solution(commands):
    answer = []
    
    # 초기 표
    table = [[["EMPTY", [[j, i]]] for i in range(51)] for j in range(51)]
    
    for command in commands:
        data = list(command.split())
        
        if data[0] == "UPDATE":
            if len(data) == 4:
                r, c, value = int(data[1]), int(data[2]), data[3]
                if len(table[r][c][1]) > 1:
                    cells = table[r][c][1]
                    for ri, ci in cells:
                        table[ri][ci][0] = value
                else:
                    table[r][c][0] = value
            else:
                value1, value2 = data[1], data[2]
                for ri in range(1, 51):
                    for ci in range(1, 51):
                        if table[ri][ci][0] == value1:
                            table[ri][ci][0] = value2
                                    
        elif data[0] == "MERGE":
            r1, c1, r2, c2 = int(data[1]), int(data[2]), int(data[3]), int(data[4])
            if table[r1][c1][1] == table[r2][c2][1]:
                continue
            elif table[r1][c1][0] == "EMPTY" and table[r2][c2][0] == "EMPTY":
                merge_cells = table[r1][c1][1] + table[r2][c2][1]
                for nr, nc in merge_cells:
                    table[nr][nc][1] = merge_cells
            elif table[r1][c1][0] == "EMPTY" and table[r2][c2][0] != "EMPTY":
                merge_cells = table[r1][c1][1] + table[r2][c2][1]
                for nr, nc in merge_cells:
                    table[nr][nc][0] = table[r2][c2][0]
                    table[nr][nc][1] = merge_cells
            else:
                merge_cells = table[r1][c1][1] + table[r2][c2][1]
                for nr, nc in merge_cells:
                    table[nr][nc][0] = table[r1][c1][0]
                    table[nr][nc][1] = merge_cells
            
        elif data[0] == "UNMERGE":
            r, c = int(data[1]), int(data[2])
            value = table[r][c][0]
            merge_cells = table[r][c][1]
            for nr, nc in merge_cells:
                if nr == r and nc == c:
                    table[nr][nc] = [value, [[nr, nc]]]
                else:
                    table[nr][nc] = ["EMPTY", [[nr, nc]]]
        
        elif data[0] == "PRINT":
            r, c = int(data[1]), int(data[2])
            answer.append(table[r][c][0])
    
    return answer