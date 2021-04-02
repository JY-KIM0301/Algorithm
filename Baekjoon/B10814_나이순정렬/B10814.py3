import sys
num = int(sys.stdin.readline())
member = []    # member 이름을 가진 배열 생성
for i in range(num):
	[x, y] = sys.stdin.readline().split()
	member.append([x, y])    # member에 [x, y] 넣어주기
result = sorted(member, key= lambda member: int(member[0]))
for i in range(num):
	print(result[i][0], result[i][1])