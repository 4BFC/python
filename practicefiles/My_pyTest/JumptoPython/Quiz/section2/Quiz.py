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

# 4
pin = "960214-1234567"
print(pin[7:8])

# 5
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)

# 6
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# 7 ☆
start = '☆'
a = ['Life', 'is', 'too', 'short']
result = ','.join(a).replace(',',' ')
print(result)

# 8 ☆☆
a = (1,2,3)
a
print(a)