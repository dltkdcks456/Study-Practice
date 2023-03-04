'''
할인율은 10%, 20%, 30%, 40% 중 하나
브루트포스로 진행해보기
1. 이모티콘 플러스 서비스 가입수가 우선
2. 판매액 그 다음
이모티콘 할인율 적용 Max 경우의 수는 : 4 ^ 7 -> 16384

'''

def solution(users, emoticons):
    sale = [10, 20, 30, 40]
    chosen = [0] * len(emoticons)
    max_service_users = max_sum_sales = 0
    
    def max_case(users_cnt, total_price):
        nonlocal max_service_users, max_sum_sales
        if max_service_users < users_cnt:
            max_service_users = users_cnt
            max_sum_sales = total_price
        elif max_service_users == users_cnt and max_sum_sales < total_price:
            max_sum_sales = total_price
            
    
    def user_case():
        nonlocal max_service_users, max_sum_sales
        service_users = sum_sales = 0
        
        for user_percent, limit_price in users:
            sum_price = 0
            for i in range(len(emoticons)):
                if chosen[i] >= user_percent:
                    sum_price += (emoticons[i] * (100 - chosen[i])) // 100
            
            if sum_price >= limit_price:
                service_users += 1
            else:
                sum_sales += sum_price
        max_case(service_users, sum_sales)
    
    def sale_case(n, m):
        if n == m:
            user_case()
            return
        else:
            for percent in range(4):
                chosen[n] = sale[percent]
                sale_case(n + 1, m)
    
    sale_case(0, len(emoticons))
    answer = [max_service_users, max_sum_sales]
    return answer