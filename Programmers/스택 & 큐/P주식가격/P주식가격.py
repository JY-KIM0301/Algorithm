from collections import deque
def solution(prices):
    answer = []
    
    prices = deque(prices)
    while prices:
        n = prices.popleft()
        cnt = 0
        for i in prices:
            if n > i:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer