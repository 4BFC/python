import sys
import heapq
input = sys.stdin.readline
#완전 트리를 이해해야함
def heapSort(iterable):
    h = []
    result = []
    #모든 원소들을 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    #힙에 삽입된 모든 워소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n) :
    arr.append(int(input()))

res = heapSort(arr)

for i in range(n):
    print(res[i])