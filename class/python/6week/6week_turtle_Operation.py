import turtle
t = turtle.Turtle()
t.shape("turtle")

w = turtle.textinput("가로입력", "가로 길이를 입력하세요")
h = turtle.textinput("세로입력", "세로 길이를 입력하세요")

area = int(w) * int(h)

w = int(w)
h = int(h)

t.forward(w)
t.left(90)
t.forward(h)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h)
t.penup()
t.goto(w, h)
t.write("사각형의 면적은 " + str(area))
