#기초 구조
numbers = [2,2,9,4,7]
for number in numbers:
    print("number: {}".format(number))

#enumerate를 사용한 경우
favor_fruit = ["사과","바나나","딸기","오렌지"]

for i, f_f in enumerate(favor_fruit) : #enumerate는 i를 넣어야 순서가 전달이 된다.
    print("{}번째 최애 과일은 {}입니다.".format(i, f_f))

#list를 사용하는 경우
number = [1,2,3,4,5]

#range는 정말 범위를 지정한다. 
for element in range(5):
    print(element)

#range의 응용
for element in range(len(number)):
    print(element)

string = "안녕,반가워"

for i, st_r in enumerate(string) :
    print("{}번째 단어는 '{}' 입니다.".format(i, st_r))
    
print("string변수 단어의 총 개수는 {}입니다.".format(len(string)))

string[0] = '해'
print(string[0])