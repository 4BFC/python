#test
import turtle
t =turtle.Turtle()
t.shape("turtle")

t.up()
t.forward(-200)
t.right(90)
t.forward(100)
t.down()
t.write("forward" + str(t.position()))
t.circle(50)
t.hideturtle()
