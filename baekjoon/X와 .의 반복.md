# X와 .의 반복

⚪**Silver 5단계 1343번 2회시도**

- 생각보다 까다로운 조건...
- 식이 복잡하며 간단한 경우를 생각하지 못함.

```python
poli = input()

# 같은 문자끼리 더해주고 다른 문자가 나오면 리스트가 추가되고 해당 덧셈 반복.
X_list = [1] # 첫 숫자는 기본값으로 가져감.
for i in range(1, len(poli)):
    if poli[i] == poli[i - 1]: # 이전 값과 같은 지 확인
        X_list[-1] += 1
    else:
        X_list.append(1)

# 제일 처음에 X인지 .인지 확인
if poli[0] == 'X':
    poli_str = '' # 출력해줄 결과값
    for j in range(len(X_list)):
        if j % 2: # 짝수는 .이 등장
            poli_str += '.' * X_list[j]
        else: # 홀수는 AAAA와 BB가 들어갈 공간
            if X_list[j] % 2 != 0: # 홀수가 나올 경우 -1을 출력
                poli_str = -1
                break
            else: # 짝수일 경우 AAAA부터 우선 출력 후 BB 출력 진행
                poli_str += 'AAAA' * (X_list[j] // 4) + 'BB' * ((X_list[j] % 4) // 2)
else: # .이 먼저올 때의 경우, 위 경우와 반대 상황
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

print(poli_str) # 결과값 출력!!!
```

