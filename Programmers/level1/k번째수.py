# date: 2021/07/17
# level: 1
# link: https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        slicing = array[i - 1: j]
        slicing.sort()
        answer.append(slicing[k - 1])
    return answer


# 다른사람 풀이
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        sliced = array[commands[i][0]-1: commands[i][1]]
        sliced.sort()
        answer.append(sliced[commands[i][2] - 1])
    return answer


# 다른사람 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
"""
map과 lambda 사용해서 한줄로 끝낸사람.. 람다는 항상 이론은 아는데 활용을 못하고
이문제에서 map을 사용할 생각도 전혀 못함 

# map과 lambda 사용한 간단예제
arr = [1,2,3]
result = list(map(lambda x:x+5, arr))
print(result) 

# 실행결과
[6,7,8]
"""
