A = [1, 5, 2, 3, 6, 2, 3, 7, 3, 5, 2, 6]
N,L = 12,3
D = []

for i in range(len(A)):
    d = i - L + 1
    if A[d:i] : #비어 있는 시퀸스가 전달 되는 것을 막기위함
        print(min(A[d:i]))
    # print(f'{A[d:i]}/{d}')
   

#최솟값 구하기
# for i in range(N):
#     n = i-L+1
#     value = A[i : n]
#     MIN = min(value)
#     # MIN = min()
#     D.append(MIN)
# print(D)