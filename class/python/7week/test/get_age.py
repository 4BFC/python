import time

now = time.time()
thisYear = int(1970 + now // (365*24*3600))
birthYear = int(input("태어난 년도 입력>> "))
age = thisYear - birthYear + 1

print("올해 :", thisYear)
print("당신의 나이 :", age)
