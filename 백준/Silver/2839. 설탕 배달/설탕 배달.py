N = int(input()) # 배달되어야하는 kg
sugar_bynyl = [3, 5] # 봉투 3kg, 5kg
least_bynyl = 0 # 가져가야할 봉투 초기값
for i in range(N // 5, -1, -1): # 5kg으로 들고갈 수 있는 최대 개수부터
    rest_sugar = N - i * 5
    if rest_sugar % 3 == 0:
        least_bynyl = i + rest_sugar // 3 # 5kg을 사용하고 남은 설탕이 3으로 나누어떨어지면 최소 봉투 개수 만족
        break
    else:
        continue
if least_bynyl == 0:
    print(-1)
else:
    print(least_bynyl)    