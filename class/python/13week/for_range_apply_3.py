import turtle
import random
turtle.colormode(255)
t = turtle.Turtle()
t.speed(8)

radius = 150

for n in range(5): #(1,150,-30)
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    t.fillcolor(r,g,b) #random값을 가지고 와서 각 fillcolor의 r,g,b값에 부여한다.
    t.begin_fill() #색상을 체우기 위해서는 해당 구문이 필요하다.
    
    t.circle(radius)
    t.end_fill()
    radius -= 30
    
