import turtle as t

def draw_circle(x,y,radius):
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(radius)

draw_circle(100,50,100)
draw_circle(-100,50,40)
draw_circle(100,-50,30)
draw_circle(-100,-50,70)
