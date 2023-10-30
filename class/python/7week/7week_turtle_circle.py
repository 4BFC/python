import turtle
t = turtle.Turtle()
t.shape("turtle")

r = turtle.textinput("반지름 입력", "반지름을 입력하세요")
space = turtle.textinput("간겨을 입력", "간격을 입력하세요")

'''
r = int(turtle.textinput("반지름 입력", "반지름을 입력하세요"))
space = int(turtle.textinput("간겨을 입력", "간격을 입력하세요"))

'''

#1st
t.circle(int(r))

#move
t.up()
t.goto(int(space), 0)
#t.forward(space)
t.down()

#2nd
t.circle(int(r))

#move
t.up()
t.goto(int(space)*2, 0)
t.down()

#3rd
t.circle(int(r))
#t.fd(int(3 * r + space))
#for문을 사용해서 응용하기
