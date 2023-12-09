import turtle as turtle, random

turtle.colormode(255)
t = turtle.Turtle()
t.speed(0)

def star(length):
    for n in range(5):
        t.forward(length) #forward와 goto차이는?
        t.left(144)

def s_draw(x,y):
    turtle.bgcolor("black")
    s_length = random.randint(1,50)

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    
    t.up()
    t.goto(x,y)
    t.down()
    t.color(r,g,b)
    t.begin_fill()
    star(s_length)
    t.end_fill()
    t.hideturtle()
    
scr = turtle.Screen()
scr.onclick(s_draw)
