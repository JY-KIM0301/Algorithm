'''
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성
'''

import math

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        divisor_count = 0 
        for divisor in range(1, int(math.sqrt(num))+1):
            if num % divisor == 0:
                if num // divisor == divisor:
                    divisor_count += 1
                else:
                    divisor_count += 2
            
        if divisor_count % 2 == 0:
            answer += num
        else:
            answer -= num
    
    return answer
