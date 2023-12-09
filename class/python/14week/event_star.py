import turtle as turtle
t = turtle.Turtle()
turtle.bgcolor("black")

def star(length):
    for n in range(5):
        t.forward(length) #forward와 goto차이는?
        t.left(144)

def s_draw(x,y):
    
    t.up()
    t.goto(x,y)
    t.down()
    t.color("yellow")
    t.begin_fill()
    star(50)
    t.end_fill()

scr = turtle.Screen()
scr.onscreenclick(s_draw)
