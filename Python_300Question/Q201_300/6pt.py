# 251 ~ 260
# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.

# 정답확인

'클래스 : 붕어빵 틀과도 같은 개념 즉, 틀을 만들어 놓는 것. 인스턴스하기 전 만들어 놓은 틀과도 같다.'
'객체 : 클래스를 통해 인스턴스화 되면서 여러 객체들을 만들어 놓는 것 '
'인스턴스 : 클래스를 객체로 만들기 위함이다. '

#ref 
'클래스 : 객체를 만들어 내기 위한 설계도 혹은 틀'
'객체 : 소프트웨어 세계에 구현할 대상'
'인스턴스 : 설계도를 바탕으로 소프트웨어 세계에 구현된 구체적인 실체'
#https://gmlwjd9405.github.io/2018/09/17/class-object-instance.html

# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.

# 정답확인

# class Human :
#   '''Human'''
#   pass

# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
# 정답확인

# areum = Human()

# 254 클래스 생성자-1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.

# >>> areum = Human()
# 응애응애
# 정답확인

# class Human :
#   print('응애응애')

# areum = Human()
#print(areum)

# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
# 정답확인

class Human :
  def __init__(self, name, age, gen):
    self.name = name
    self.age = age
    self.gen = gen

areum = Human("조아름", 25, "여자")

print(areum.name)

# 256 인스턴스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

# 이름: 조아름, 나이: 25, 성별: 여자
# 인스턴스 변수에 접근하여 값을 가져오는 예

# >>> areum.age
# 25
# 정답확인

print("이름 : {}, 나이 : {}, 성별 : {}".format(areum.name, areum.age, areum.gen))

# 257 클래스 메소드 - 1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

# >>> areum.who()
# 이름: 조아름, 나이: 25, 성별: 여자
# 정답확인
print("-"*8)
class Human :
  def who():
    print("이름: 조아름, 나이: 25, 성별: 여자")
Human.who()

#solution
print("-"*8,"solution")
class Human :
  def __init__(self, name, age, gen):
    self.name = name
    self.age = age
    self.gen = gen
  def who(self):
    print("이름: {}, 나이: {}, 성별: {}".format(self.name,self.age, self.gen))

areum = Human("아름", 25, "여자")
areum.who()

# 258 클래스 메소드 - 2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
# >>> areum = Human("모름", 0, "모름")
# >>> areum.setInfo("아름", 25, "여자")
# 정답확인

print("-"*8)
class Human :
  def __init__(self, name, age, sex) -> None:
    self.name = name
    self.age = age
    self.sex = sex
  def setInfo(self, name, age, sex) :
    self.name = name
    self.age = age
    self.sex = sex

areum = Human("모름",0,"모름")
areum.setInfo("아름", 25, "여자")

#solution
print("-"*8,"solution")
class Human :
  def __init__(self, name, age, gen):
    self.name = name
    self.age = age
    self.gen = gen
  def who(self):
    print("이름: {}, 나이: {}, 성별: {}".format(self.name,self.age, self.gen))
  def setInfo(self, name, age, gen) :
    self.name = name
    self.age = age
    self.gen = gen


areum = Human("모름",0,"모름")
areum.who()
areum.setInfo("아름", 25, "여자")
areum.who()

# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")
# >>> del areum
# 나의 죽음을 알리지 말라
# 정답확인

print("-"*8,"solution")
class Human :
  def __init__(self, name, age, gen):
    self.name = name
    self.age = age
    self.gen = gen
  def who(self):
    print("이름: {}, 나이: {}, 성별: {}".format(self.name,self.age, self.gen))
  def setInfo(self, name, age, gen) :
    self.name = name
    self.age = age
    self.gen = gen
  def __del__(self) :
    print("나의 죽음을 알리지 마라.")

areum = Human("아름", 25, "여자")
del areum

# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.

# class OMG : 
#     def print() :
#         print("Oh my god")

# >>> >>> myStock = OMG()
# >>> myStock.print()
# TypeError Traceback (most recent call last)
# <ipython-input-233-c85c04535b22> in <module>()
# ----> myStock.print()

# TypeError: print() takes 0 positional arguments but 1 was given
# 정답확인

class OMG : 
  def print(self) :
    print("Oh my god")

myStock = OMG()
myStock.print() #print가 이미 존재하기 때문인가?
