import sys
input = sys.stdin.readline

'''
만약 이전의 숫자와 합해져서 만들어지는 단어가 2개가 된다면,
피보나치수열과 같은 느낌으로 진행된다.
ex) 1 2 인경우
1, 2
12
로 2가지 경우가 나타내어지는데 이때 위의 경우에는 1까지 나타날 수 있는 경우의 수가 그대로 오면 되고
그 다음에는 1 이전의 개수를 더해주면 된다.
'''

text = [0] + list(map(int, input().rstrip()))
dp = [0] * (len(text) + 1)
dp[0] = 1
dp[1] = 1

if len(text) == 1 or text[1] == 0:
    print(0)
else:
    for i in range(2, len(text)):
        if i < len(text) - 1 and (text[i] * 10 + text[i + 1] == 10 or text[i] * 10 + text[i + 1] == 20):
            dp[i] = dp[i - 1]
        elif text[i] == 0 and (text[i - 1] >= 3 or text[i - 1] == 0):
            dp[-2] = 0
            break
        elif text[i] == 0 and (text[i - 1] == 1 or text[i - 1] == 2):
            dp[i] = dp[i - 1]
        elif text[i - 1] !=0 and 1 <= text[i - 1] * 10 + text[i] <= 26:    # 2가지의 경우의 수가 나오는 경우
            dp[i] = dp[i - 2] + dp[i - 1]
        else:
            dp[i] = dp[i - 1]
    print(dp[-2] % 1000000)