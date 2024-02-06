# import sys
# input = sys.stdin.readline
n = int(input())
N = list(map(int, input().rstrip())) # rstrip()을 사용하여 개행 문자 제거
if n == len(N):
    print(sum(N))
