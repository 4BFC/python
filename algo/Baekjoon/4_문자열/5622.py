# 2차원 배열로 풀려 했음
N = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '']  # 11
print(len(N)+1)  # total time
T = input()
if T[0] in 'Q':
    print(T.index('Q'))
# for _ in range(len(T)):
#     print(T[_])
for i in range(len(N)):
    for ii in range(len(N[i])):
        # print(N[i][ii])
        if T.index('Q') == True:
            print(i, ii)
            print('check')
# print(N[1][0])
