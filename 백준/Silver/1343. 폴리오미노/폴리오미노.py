poli = input()
X_list = [1]
for i in range(1, len(poli)):
    if poli[i] == poli[i - 1]:
        X_list[-1] += 1
    else:
        X_list.append(1)

if poli[0] == 'X':
    poli_str = ''
    for j in range(len(X_list)):
        if j % 2:
            poli_str += '.' * X_list[j]
        else:
            if X_list[j] % 2 != 0:
                poli_str = -1
                break
            else:
                poli_str += 'AAAA' * (X_list[j] // 4) + 'BB' * ((X_list[j] % 4) // 2)
else:
    poli_str = ''
    for j in range(len(X_list)):
        if j % 2 == 0:
            poli_str += '.' * X_list[j]
        else:
            if X_list[j] % 2 != 0:
                poli_str = -1
                break
            else:
                poli_str += 'AAAA' * (X_list[j] // 4) + 'BB' * ((X_list[j] % 4) // 2)

print(poli_str)