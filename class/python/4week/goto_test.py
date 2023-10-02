#test
import turtle
t =turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(-200,-100)
t.down()
t.write("goto" + str(t.position()))
t.circle(50)
t.hideturtle()
