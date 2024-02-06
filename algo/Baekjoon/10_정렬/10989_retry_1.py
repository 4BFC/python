import sys 
input = sys.stdin.readline
N = []
n = int(input())

for _ in range(n):
    N.append(int(input()))
#append는 메모리가 재할당이 되면서 메모리를 효율적으로 사용하지 못한다.
N.sort()

for i in range(n):
    print(N[i])
# 메모리 초과 : https://wikidocs.net/21057
# 계수 정렬 : https://kill-xxx.tistory.com/entry/python-%EA%B3%84%EC%88%98%EC%A0%95%EB%A0%AC