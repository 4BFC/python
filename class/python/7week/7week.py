#연산자
a = 7
b = 5
print(a+b, a-b, a*b, a/b)
print(a/b,a//b,a%b, a**b)#나누기,몫,나머지,제곱
#1.4,?,2

#리스트
data = [10, 20, 30, 40]
sum = data[0] + data[1] + data[2] + data[3]
print("합계 = ", sum)
'''
for list in range(len(data)):
    print(data[list])
'''

PI = 3.14 #상수
radius = float(input("반지름을 입력 : "))
area = PI * radius ** 2
around = 2 * PI * radius
print("원의 면적은 ", area, "이고, 원의 둘래는", around, "입니다.")
