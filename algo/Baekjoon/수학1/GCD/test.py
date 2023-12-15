# 최대공약수 : 두 수의 공통 약수 중 가장 큰 것
# A, B = map(int, input().split())  # 10, 3 => 1
for i in range(min(10, 3), 0, -1):
    print(i)
    if i % 10 == 0 and i % 3 == 0:
        print('----------')
        print(f"10 % {i} => {10 % i}")
        print(f"3 % {i} => {3 % i}")
        print(i)
        break
