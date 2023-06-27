#from Programmers : python입문편 - method

class Human :
  '''인간'''
  def create(name,weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person
#클래스안에서의 함수들의 매개변수는 self로 사용한다.
  def eat(self) :
    self.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))

  def walk(self) :
    self.weight -= 0.1
    print("{}가 걸어서 {}kg이 되었습니다.".format(self.name, self.weight))
#def를 통한 함수가 아닌 init만 존재하면서 이런 식으로 클래스를 사용 가능한것 인가?
  def speak(self, message):
    print(message)

#만약 eat함수가 밖으로 나와 있다면 매개변수로 person을 넣어야 한다.
def eat(self) :
    self.weight += 0.1
    print("{}가 먹어서 {}kg이 되었습니다.".format(self.name, self.weight))

person = Human.create('철수', 60.5)

print(person.name)
print(person.weight)

eat(person) #밖에 있는 eat함수를 사용할 때이다.(매개변수를 사용하지 않는 방법은 아래와 같다.)
person.eat() #person이라는 인스턴스가 eat에 자동으로 매개변수에 self로 들어가진다.
person.speak('안녕하셔요') #person.eat()과 같다.

person.walk()
person.eat()
person.walk()