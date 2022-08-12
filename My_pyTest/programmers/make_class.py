#from Programmers : python입문편 - class
class Human :
  def __init__(self) -> None:
    pass

# def __init__(self)는 클래스가 생성시 기본적으로 실행되는 함수이다.

person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'
person1.name = '서울시민'
person2.name = '인도인'

def speak(person) : 
  print("{}이 {}로 말을 합니다.".format(person.name, person.language))

Human.speak = speak #함수를 Human클래스에 추가한 것이다.

print('test')
speak(person1)
speak(person2)



print(person1.speak())
print(person2.speak())