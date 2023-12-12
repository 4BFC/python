#test
import turtle
t =turtle.Turtle()
t.shape("turtle")

t.up() #팬을 들고
t.goto(-200,-100) #원하는 곳으로 이동
t.down() #팬을 다운
t.write("goto" + str(t.position())) #좌표를 찍어주는 함
t.circle(50) #해당 위치로 옮겨진 팬은 그림을 그린다.
t.hideturtle() #해당 커서를 감추는 함수
