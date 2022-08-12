#from Programmers : python입문편 - modeling

class Human :
  # def __init__(self) -> None:
  #   pass
  '''인간'''
#def를 통한 함수가 아닌 init만 존재하면서 이런 식으로 클래스를 사용 가능한것 인가?

person = Human()
person.name = "안식년"
print(type(person))

def create_human(name,weight):
  person = Human()
  person.name = name
  person.weight = weight
  return person

Human.create = create_human
person = Human.create('철수', 60.5)

def eat(person) :
  person.weight += 0.1
  print("{}가 먹어서 {}kg이 되었습니다.".format(person.name, person.weight))

def walk(person) :
  person.weight -= 0.1
  print("{}가 걸어서 {}kg이 되었습니다.".format(person.name, person.weight))


Human.eat = eat
Human.walk = walk

person.walk()
person.eat()
person.walk()