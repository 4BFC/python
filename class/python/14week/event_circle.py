import turtle as t

sc = t.Screen()

def draw_circle(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(100)

sc.onclick(draw_circle)

sc.mainloop()
        
