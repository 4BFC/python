# a, b = ('python', 'life')
# print("a = {} b = {}\n".format(a,b))
# (a, b) = 'python', 'life'
# print("a = {} b = {}\n".format(a,b))
# [a,b] = ['python', 'life']
# print("a = {} b = {}\n".format(a,b))
# a = b = 'python'
# print("a = {} b = {}\n".format(a,b))
#test

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