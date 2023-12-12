#test
import turtle
t =turtle.Turtle()
t.shape("turtle")

t.up()
#팬을 현재 들려 있는 상태이다.
t.forward(-200) #goto와 다르게 x,y를 따로 작성해서 움직여야 한다.
t.right(90)
t.forward(100) #goto와 다르게 x,y를 따로 작성해서 움직여야 한다.
t.down()
#팬이 현재 다운 되어 있다.

t.write("forward" + str(t.position()))
t.circle(50)
t.hideturtle()
