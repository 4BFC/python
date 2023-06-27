'''컴프리핸션의 사용'''

#dict
testlist = {1:'a',2:'b'}
print(testlist.keys())
print(testlist,type(testlist))


#list
students = ['동우', '관중', '명훈', '현배']
for number, name in enumerate(students):
  print("{}번의 이름은 {}입니다.".format(number+1,name))

print(students)

students_dict = {"{}번".format(number+1) : name for number,name in enumerate(students)} #생긴것이 dict와 비슷하게 생겼다.. 그렇다 dict다!! list를 dict로 만든 것이다.
print(students_dict, type(students_dict)) #

#zip
scores = [80,90,40,78]

for x,y in zip(students, scores):
  print(x,y)

scores_dict = {student : scores for student, score in zip(students,scores)}
print(scores_dict, type(scores_dict))

product_list = ["풀", "가위", "크래파스"]
price_list = [800, 2500, 5000]
product_dict = {product : price for product, price in zip(product_list, price_list)}

print(product_dict)