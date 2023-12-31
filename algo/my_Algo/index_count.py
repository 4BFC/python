N = '1 2 3 4 5'

print(N)  # str
n = N.split(' ')  # list
print(n)  # list

print(f"index : {N.index('1')}")
print(f"count : {N.count('1')}")

for i in n:  # list의 모든 element를 i로 반환한다.
    print(i, end=" ")
# for 문을 돌리면서 i로 반환 받은 element들의 index값을 새로 받아 볼 것.
New_n = []  # index 정보를 받아오는 list영역
for i in n:
    print(i, end=" ")  # i type is str
    # 예상은 [0,1,2,3,4]가 나올 것이다. 하지만 [0, 2, 4, 6, 8]가 나온다.
    # 그 이유는 N = '1 2 3 4 5'에서 space영역을 포함해서 값을 비교 분석하기 때문이다.
    # 따라서 str을 list로 재가공을 하거나 split이나 replace를 사용해서 새롭게 선언해야한다.
    New_n.append(N.index(i))

print(New_n)
print()
print()

# str을 list로 가공 했을 때의 모습이다.
N = 'ObjectOrientedProgramming1 3.0 A+'
if 'A+' in N:
    print('exit')
print(f"{N} => {type(N)}")
N = N.split()
print(f"{N} => {type(N)}")

New_n = []
for i in N:
    print(i, end=' / ')
    New_n.append(i)

print(New_n)

print(New_n)
for i in New_n:
    if 'A+' in i:
        print('exit')
        print(New_n.index(i))
