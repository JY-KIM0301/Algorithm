'''
https://programmers.co.kr/learn/courses/18/lessons/1878

직사각형을 만드는데 필요한 4개의 점 중 3개의 좌표가 주어질때, 나머지 한 점의 좌표를 반환하는 함수 작성.

v                      
----------------------
[[1,4], [3,4], [3,10]] 

result
----------------------
[1,10]
'''

# 결과값으로 반환될 좌표는 입력된 세개의 좌표중, x와 y좌표에서 한번만 나온 값이다. 
# 이중 리스트를 쪼개서 x와 y리스트에 각각 x, y 값을 넣어주고 중복된값은 제거시켜서 x, y리스트에 한번만 나온 값만 남아있도록 한다. 

def solution(v):
  # x, y좌표가 들어갈 리스트
  x = []
  y = []
  
  # 입력된 이중 리스트 탐색 
  for i in v:
    x.append(i[0])
    y.append(i[1])
    
    # x좌표 리스트에 똑같은 값이 두개있다면
    if x.count(i[0]) == 2:
      # set()을 사용해 중복을 제거, list로 변환후 제거한다 
      x = list(set(x))
      x.remove(i[0])
      
    # y좌표: x와 동일하게 수행
    if y.count(i[1]) == 2:
      y = list(set(y))
      y.remove(i[1])
  
  # x와 y리스트 연결
  x.extend(y)
  return x 
