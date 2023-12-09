import turtle
t = turtle.Turtle()
#원형 그리
t.circle(50)

t.goto(100,0)
#삼각형 그리
for n in range(3):
    t.forward(100)
    t.left(120)
