# import sys
# input = sys.stdin.readline
N,M = map(int,input().split()) # N,M Size

A,B= [],[]
# B = []
# result = []
for _ in range(N):
    a = list(map(int,input().split()))
    A.append(a)
    
for _ in range(N): #M애서 N으로 바꾸니깐 정상적으로 작동한다. 무슨 차이이지?
    b = list(map(int,input().split()))
    B.append(b)
    
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=" ")
    print()
#         r.append(A[i][j] + B[i][j])
#     result.append(r)
# # print(result)

# for i in range(N) :
#     print(*result[i])