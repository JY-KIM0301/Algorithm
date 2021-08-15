# date: 2021/08/13
# level: 2
# description: Hash
# link: https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    dic = {}
    for i in record:
        temp = i.split()
        if temp[0] == "Enter" or temp[0] == "Change":
            dic[temp[1]] = temp[2]
        else:  # Leave
            continue
    for i in record:
        temp = i.split()
        if temp[0] == "Enter":
            answer.append(dic[temp[1]] + "님이 들어왔습니다.")
        if temp[0] == "Leave":
            answer.append(dic[temp[1]] + "님이 나갔습니다.")
        else:  # Change
            continue
    return answer