#from Programmers : python입문편 - method

class Human :
  '''인간'''
  def __init__(self,name,weight) -> None:
    '''초기화 함수'''
    print("__init__실행")
    self.name = name
    self.weight = weight
    print("이름은 {} 몸무게는 {}".format(name,weight))

  def __str__(self) -> str:
    '''문자열화 함수'''
    return "{} (몸무게 {}kg)".format(self.name,self.weight)
    #인스턴스 자체를 출력할 때의 형식을 지정해주는 함수
  
  # def create(name,weight):
  #   person = Human()
  #   person.name = name
  #   person.weight = weight
  #   return person
    
  def eat(self) :
    self.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))

  def walk(self) :
    self.weight -= 0.1
    print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))


person = Human("사람",70)
#이전(person = Human.create('철수', 60.5))과는 달리 간단해졌다.
print(person.name)
print(person.weight)

