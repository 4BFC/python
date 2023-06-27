# a, b = ('python', 'life')
# print("a = {} b = {}\n".format(a,b))
# (a, b) = 'python', 'life'
# print("a = {} b = {}\n".format(a,b))
# [a,b] = ['python', 'life']
# print("a = {} b = {}\n".format(a,b))
# a = b = 'python'
# print("a = {} b = {}\n".format(a,b))
#test

from msvcrt import kbhit


numbers = [(1, 2), (10, 0)]
for a,b in numbers:
    print("a = {} b = {}".format(a,b))

for i in range(10):
    if i % 2 ==0: #2,4,6,8
        continue
    print(i)#1,3,5,7,9


numbers = [(1, 2), (10, 0)]

for a, b in numbers:
    if b == 0:
        print("0으로 나눌 수는 없습니다.",b)
        continue
    print("{}을(를) {}로 나누면 {}".format(a, b, a/b))


num = 5
myn = 'ㄱ'
pi_v = 3.14
print("나는 연습을 %d번 했다." % num)
print("나의 성씨 초성은 '%c'이다." % myn)
print("나는 파이의 값이 %0.3f로 알고 있다." % pi_v)

print("나는 연습을 %d번 했다. 나의 성씨 초성은 '%c'이다." % (num,  myn))

a = [1,2,3,4]   #list
result = []     #list

for num in a:
    result.append(num*3) #3,6,9,12
print(result)

print(type({})) # dict
print(type(())) # tuple
print(type([])) # list

tmp = 0
for i in range(0,11):
    tmp += i
    print(tmp)


tmp = 0
result=[]
for i in range(0,11):
    tmp += i
    result.append(tmp)
print(result)

for my_list in [1,2,3,0] :
    print(my_list)
    if (my_list%2) == 0 :
        print("조건에 해당됩니다. 중지합니다.")
        break
    print("before=",my_list)
print("result=",my_list) #마지막 값이 나온다.

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: 
        continue
    print(a)

    shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}
try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product =='풀':
                print("{}: {}원".format(shop, price))
                raise StopIteration
except StopIteration:
    print("정상종료")
