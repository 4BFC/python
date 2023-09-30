import turtle
t =turtle.Turtle()
t.shape("turtle")
'''
#도형 여러개 그리기
t.circle(100)
t.circle(70,360,6)
#t.fillcolor("black")
t.fillcolor(255,255,255)
#다르게 시도하기
t.begin_fill()
t.circle(20,360,3)
t.end_fill()
t.hideturtle()
'''

#오륜기 그리기
#150이동

t.pensize(5)
t.speed(5)
turtle.colormode(255)

#t.color(0,0,255)
#1st
t.color(0,0,255)
t.up()
t.goto(-150,50)
t.down()

t.circle(70)

#2nd
t.color(0,0,0)
t.up()
t.goto(0,50)
t.down()

t.circle(70)

#3rd
t.color(255,0,0)
t.up()
t.goto(150,50)
t.down()

t.circle(70)

#4th
t.color(0,255,0)
t.up()
t.goto(75,-50)
t.down()

t.circle(70)

#5th
t.color(255,255,0)
t.up()
t.goto(-75,-50)
t.down()

t.circle(70)

