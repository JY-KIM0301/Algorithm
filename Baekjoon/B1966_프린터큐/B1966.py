test_case = int(input())

for _ in range(test_case):
	n, m = list(map(int, input().split()))
	imp = list(map(int, input().split()))    # 중요도 
	idx = list(range(len(imp)))    # 문서마다 고유 인덱스 생성 
	idx[m] = 'target'

	order = 0    # 순서

	while True:
		if imp[0] == max(imp):    
			order += 1    # 최대 중요도 순서대로 인쇄
			
			if idx[0] == 'target':    # idx의 첫번째 값이 target인 경우 
				print(order)            # 해당 인쇄순서 출력
				break
			else:
				imp.pop(0)
				idx.pop(0)
		else: 
			imp.append(imp.pop(0))
			idx.append(idx.pop(0)) 