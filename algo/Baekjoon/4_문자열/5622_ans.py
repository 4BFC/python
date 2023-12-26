dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# a = ['TEST']  # -> False가 나옴 : 여기서 a[j]가 받는 값은 list의 첫번 째 인자 전부인 TEST이다. 즉, list로 한번 감쌌기 때문이다. 아래 a = 'TEST'로 변경하면 된다.
a = 'TEST'
# a = input()  # -> True
ret = 0
for j in range(len(a)):
    for i in dial:
        print(f"{type(a[j])}, {type(i)} / {a[j]}, {i} => ", end=" ")
        print(a[j] in i)  # 묶음으로도 in은 읽는다..
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)
