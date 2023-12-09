import turtle, random
#게임을 응용하는 시험이 나올 수도 있음
sc = turtle.Screen()
image1 = "car1.gif"
image2 = "car2.gif"
sc.addshape(image1) #addshape의 역할은? turtle의 shape 모양을 추가하는 코드
sc.addshape(image2)

def player(image, no):
    t = turtle.Turtle()
    t.shape(image) #선을 그려내는 화살표를 이미지로 만들었다.(addshape으로 값을 지정해야한다.)
    t.pensize(3)
    t.penup() #위치를 지정할 때는 팬을 들어서 움직이는 선을 보이지 않게 한다.
    t.goto(-sc.canvwidth, -200*(no-1)) #위치 지정
    return t

t1 = player(image1,1)
t2 = player(image2, 2)
t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

for i in range(50):
    d1 = random.randint(1,60)
    t1.fd(d1)
    d2 = random.randint(1,60)
    t2.fd(d2)
    if (t1.pos()[0] > sc.canvwidth or
        t2.pos()[0] > sc.canvwidth): #width인 넓이 값을 가져온다. pos()[0]는 x이다.
        if(t1.pos()[0] > t2.pos()[0]):
            print("토끼 승!")
        else :
            print("거북이 승!")
        break;
print("경기 끝!")
