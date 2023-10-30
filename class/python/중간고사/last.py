import turtle
t = turtle.Turtle()
t.shape("turtle")

t.pensize(5)
t.speed(5)
turtle.colormode(255)

#t.color(0,0,255)

#삼각형 만들기
t.color(0,0,255)
t.up()
t.goto(-150,50)
t.down()
t.circle(70,360,3)

#4각형 만들기
t.color(0,200,0)
t.goto(-150,50)
t.down()
t.circle(50,360,4)

t.color(0,200,0)
t.goto(150,50)
t.down()
t.up()
t.circle(70)

#원형만들기
t.color(255,0,0)
t.goto(150,50)
t.down()
t.up
t.circle(40)

#4각형 만들기
t.color(200,205,10)
t.goto(175,50)
t.down()
t.circle(50,360,4)

#3각형 만들기
t.color(200,255,100)
t.up()
t.goto(-105,-50)
t.down()
t.circle(70,360,3)
