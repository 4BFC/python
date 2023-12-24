# N = ['', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ', '']
N = [[''], ['ABC'], ['DEF'], ['GHI'], ['JKL'],
     ['MNO'], ['PQRS'], ['TUV'], ['WXYZ'], ['']]
for i in range(len(N)):
    print(f"i = {N[i]}", end=" ")
    for ii in range(len(N[i])):
        print(f"ii = {N[i][ii]} / {N[i][ii]}", end=" ")
        print()
