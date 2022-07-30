# Memoization

⚪**Silver 3단계 1003번 10회시도**

- `0과 1`을 문자열로 받아 개수를 세어보기도 했지만, 메모리 초과로 실패
- `Memoization`없이는 해당 문제 해결하기 힘듦
  - 값을 저장할 공간을 마련하고 재활용 가능하게 만들어 준다
- 0과 1을 계산할 때도 따로 딕셔너리를 만들어서 계산을 해줌
  - 결국 0, 1의 누적 합이 피보나치의 합이기 때문에 가능

```python
T = int(input())

for i in range(T):
    n = int(input())
    fibo_memo = {0: 0, 1: 1}
    cnt0_memo = {0: 1, 1: 0}
    cnt1_memo = {0: 0, 1: 1}
    def fibo(n):
        if n in fibo_memo:
            n = fibo_memo[n]
            return n
        else:
            fibo_memo[n] = fibo(n - 1) + fibo(n - 2)
            cnt0_memo[n] = cnt0_memo[n - 1] + cnt0_memo[n - 2]
            cnt1_memo[n] = cnt1_memo[n - 1] + cnt1_memo[n - 2]
            return fibo_memo[n]
    fibo(n)
    print(cnt0_memo[n], cnt1_memo[n])
```

