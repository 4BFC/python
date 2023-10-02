import turtle
t =turtle.Turtle()
t.shape("turtle")
'''
#colormode, RGB를 사용하
turtle.colormode(255)
#도형 여러개 그리기

#기본 원형 사이즈 100
t.circle(100)

#색상 집어 넣기 준비
t.begin_fill()
#70사이즈의 360도 육각형
t.circle(70,360,6)
t.fillcolor(250,205,0)
t.end_fill()
#t.fillcolor("black")

#색상 집어 넣기 준비
t.begin_fill()
#20사이즈의 360도 삼각형
t.circle(20,360,3)
#마지막 도형에 빨강색 채워 넣기 
t.fillcolor(255,0,0)
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

