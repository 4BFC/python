import sys
# T = int(input())
T = int(sys.stdin.readline().strip())  # strip()함수를 사용함으로 개행문자 /n을 제거할 수 있다.
for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)
