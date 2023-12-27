Alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = input()

for i in Alp:
    N = N.replace(i, '*')  # input 변수와 동일한 이름의 변수
    print(N)
print(len(N))
