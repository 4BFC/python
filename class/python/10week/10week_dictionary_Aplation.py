animal_dic = {}

animal_dic['호랑이'] = 'Tiger'
animal_dic['사자'] = 'Lion'
animal_dic['코끼리'] = 'Elephant'
animal_dic['토끼'] = 'Rabbit'
animal_dic['거북이'] = 'Turtle'

word = input("호랑이, 사자, 코끼리, 토끼, 거북이 중 하나를 입력하세요:")
print(word,"영어 단어는 \n", "==>", animal_dic[word], "입니다.")
