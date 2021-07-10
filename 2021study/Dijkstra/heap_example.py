"""
heap 라이브러리 사용 예제
"""
import heapq

# 최소 힙: 오름차순 힙 정렬(Heap Sort)
def min_heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
        # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# 최대 힙: 내림차순 힙 정렬
def max_heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
        # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
result = min_heapsort(arr)
print(result)
result = max_heapsort(arr)
print(result)

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""
