# date: 2021/09/01
# problem: 신규 아이디추천 (2021 상반기 카카오 블라인드), level 1
# link: https://programmers.co.kr/learn/courses/30/lessons/72410#

# import re
'''
보자마자 정규식이다 하고 풀었지만 2단계부터 틀렸던 문제.
결론은 정규식 써서 틀렸다. 19 번째 줄이 오답의 원인이었다..
테스트케이스는 다 통과했기에 고치는데 시간이 더 오래걸렸고, 결론은 정규식 안쓰고 풀이했다.
정규표현식만 써서 풀이한 정답을 보니 정말 짧고.. 대단했지만 그걸 다 알아보고 풀시간에 하나하나 구현하는게 더 빠를것같다.
이번 문제에 나온 정규표현식이라도 꼭 알아두자.
'''
def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()

    # 2단계 (수정전 오답코드)
    # answer = re.compile('[(\w)_.-]').findall(new_id)
    # answer = ''.join(answer)

    # 2단계 수정
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i
            # 3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4단계
    for i in range(len(answer)):
        if answer[0] == '.' or answer[len(answer) - 1] == '.':
            answer = answer.strip('.')
    # 5단계
    if len(answer) == 0:
        answer = 'a'
    # 6단계
    if len(answer) > 15:
        answer = answer[:15]
    for i in range(len(answer)):
        if answer[0] == '.' or answer[len(answer) - 1] == '.':
            answer = answer.strip('.')
            # 7단계
    if len(answer) <= 2:
        temp = answer[len(answer) - 1]
        for i in range(3):
            answer = answer + temp
            if len(answer) == 3:
                break

    return answer

"""
출제자 의도가 가득담긴 풀이 

import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
"""
