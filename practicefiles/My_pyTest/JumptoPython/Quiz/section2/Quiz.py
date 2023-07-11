# 02 section
# Q1
korea = 80
english = 75
math = 55
average = (korea + english + math)/3
print(average)

# Q2
num = 13
print(num % 2)

# Q3
pin = "960214-1234567"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

# Q4
pin = "960214-1234567"
print(pin[7:8])

# Q5
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# Q6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# Q7 ☆
start = '☆'
a = ['Life', 'is', 'too', 'short']
result = ','.join(a).replace(',',' ')
print(result)

# Q8 ☆☆
#ref : https://wook1005.tistory.com/4
a = (1,2,3)
a = a + (4,); #tuple의 추가와 제거의 대한 개념
print(a)

#Q9 ☆
a = dict();
a['name'] = 'python';
print(a);
a[('a',)] = 'python';
print(a);
a[250] = 'python';
print(a);
# a[[1]] = 'python'; #list와 dict는 다르다.
# print(a);

#Q10
a={'A':90, 'B': 80, 'C' :70}
result = a.pop('B');
print(a);
print(result);

#Q11 ☆☆☆
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a);
print(aSet, type(aSet));
b = list(aSet)
print(b,type(b))

#Q12 ☆☆☆ 
a = b = [1,2,3]
a[1] = 4
print(b)
print(id(a) ,"/", id(b))
print(id(a) == id(b))
# => b는 1,4,3이 출력된다. 그리고 참조 변수이기 때문에 메모리 구조상 stack에 a,b가 존재하고 queue에는 a와 b는 같은 주소지를 가리킨다.
# id함수를 통해서 같은 주소지를 가리킨다는 것을 알 수 있다.