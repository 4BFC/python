# 최소공배수
A, B = map(int, input().split())  # 10, 3 => 30
for i in range(max(A, B), (A*B) + 1):
    print(f"i = {i}")
    if i % A == 0 and i % B == 0:
        print('----------')
        print(f"{A} % {i} => {A % i}")
        print(f"{B} % {i} => {B % i}")
        print(i)
        break
