import turtle
t = turtle.Turtle()
t.speed(8)
radius=100

for n in range(1,7) : #0,7
    t.circle(radius) #원형을 그리는 값이다.
    t.left(360/n) #화살표의 회전을 정하는 값이다.
