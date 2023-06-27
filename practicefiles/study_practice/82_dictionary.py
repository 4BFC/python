from multiprocessing.sharedctypes import Value


days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

for day in days_in_month.keys():
    print(day)

for day_value in days_in_month.values():
    print(day_value)

item_days = days_in_month.items()
print(item_days,type(item_days))
#item_days[0] = {"12월":31} #dict_items는 튜플과 같이 값 변경이 가능하지 않다.
# a = item_days.key()
# print(a)

for key, value in days_in_month.items(): #.items()는 key값과 value값 튜플 쌍 목록을 반환
    print("{}는 {}입니다.".format(key,value))
    print(key[1],key[0],type(key)) #여기서 key는 문자열이다
    print(value) #value는 값만 저장하고 담고 있을 뿐이다 즉, 키값을 통해서만 값을 불러오는 것이다.

dic1 = {'one' : 100, 'tow' : 200}
dic2 = {'one' : 1000, 'three' : 300, 'four' : 400}
dic1.update(dic2)
print("dic1.update() : ", dic1) #{'one' : 100, 'tow' : 200, 'three' : 300, 'four' : 400}
#'one'의 키 값은  dic1을 기준으로 둔다. 그래서 'one'의 value는 100이다.
dic1 = {'one' : 100, 'tow' : 200}
dic2 = {'one' : 1000, 'three' : 300, 'four' : 400}
dic2.update(dic1)
print("dic2.update() : ", dic2)
