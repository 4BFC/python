#circle

import turtle
t =turtle.Turtle()
t.shape("turtle")
'''
t.width(3)
t.color("red")
t.circle(50)
t.up()
t.forward(80)
t.down()
t.fillcolor("yellow")
t.begin_fill()
t.circle(70)
t.end_fill()
'''

#이부분을 다시 해주세요.
turtle.colormode(255)
t.pensize(3)
t.color(0,0,255)
t.fillcolor(255,255,0)
t.begin_fill()
t.circle(50)
t.end_fill()


'''
#선을 그리지 않기 위해서는 up과 down을 사용해야한다.
t.up()
t.goto(-200, 0)
t.down()
t.write("세모")
t.circle(50,360,3)
t.up()
t.goto(0,0)
t.down()
t.write("네모")
t.circle(50,360,4)
t.up()
t.goto(200,0)
t.down()
t.write("원")
t.circle(50)
t.hideturtle()
'''
