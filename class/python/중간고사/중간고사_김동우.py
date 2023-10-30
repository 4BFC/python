#1번문제
#tkinter 연결하기
from tkinter import *
root = Tk()
root.title("커피 주문받기")
root.geometry("900x500")

#row

#커피 종류  Label
lbl_kind = Label(root, text = "커피 종류")

#커피 가격 Label
lbl_price = Label(root, text = "커피 가격")

#주문수량 Label
lbl_order = Label(root, text = "주 문수량")

#생성된 Label위젯 창에 보여주는 pack
lbl_kind.pack()
lbl_price.pack()
lbl_order.pack()

#각 메뉴와 가격들을 리스트로 만든 변
order_list = ["아메리카노", "카페라떼","카페모카","쿠키"]
price_list = [2000, 3000, 3500, 5000]

lbl_a = Label(root, text = order_list[0])
lbl_p_a = Label(root, text = price_list[0])
ent_a = Entry(root, width = 27)

lbl_b = Label(root, text = order_list[1])
lbl_p_b = Label(root, text = price_list[1])
ent_b = Entry(root, width = 27)

lbl_c = Label(root, text = order_list[2])
lbl_p_c = Label(root, text = price_list[2])
ent_c = Entry(root, width = 27)

lbl_d = Label(root, text = order_list[3])
lbl_p_d = Label(root, text = price_list[3])
ent_d = Entry(root, width = 27)

lbl_person = Label(root, text = "인원")
ent_person = Entry(root, width = 27)

lbl_total = Label(root, text = "총금액")
lbl_pay = Label(root, text = "1인당 지불 금액")

#함수 구현
def pay() :
    #총계산 변수를 만든다. entry로 부터 값을 .get()함수로 가져온다. 이것들을 int로 형변화해서 가격리스트와 계산을 해준다.
    total = int(ent_a.get()) * price_list[0] + int(ent_b.get()) * price_list[1] + int(ent_c.get()) * price_list[2]+ int(ent_d.get()) * price_list[3]
    div = int(total / int(ent_person.get()))
    #젯에 있는 text를 동적으로 변환을 하려고 했으나. 변환이 되지 않았다.
    lbl_total = Label(root, text = "주문한 총금액은 "+ str(total) + "입니다.")
    lbl_pay = Label(root, text = "1인당 지불할 금액은 "+ str(div) + "원 입니다.")
    #위젯이 아닌 콘솔로 확인을 해본 결과 실행과 정상적 가격을 측정한다.
    print("주문한 총금액은 "+ str(total) + "입니다.")
    print("1인당 지불할 금액은 "+ str(div) + "원 입니다.")
    
paybtn = Button(root, text ="금액계산", command = pay)

#모든 위젯을 uiux로 보여주기위한 pack 영역이다.

lbl_a.pack()
lbl_p_a.pack()
ent_a.pack()

lbl_b.pack()
lbl_p_b.pack()
ent_b.pack()

lbl_c.pack()
lbl_p_c.pack()
ent_c.pack()

lbl_d.pack()
lbl_p_d.pack()
ent_d.pack()

lbl_person.pack()
ent_person.pack()
paybtn.pack()

lbl_total.pack()
lbl_pay.pack()

root.mainloop()

#2번 문제
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.pensize(5)
t.speed(5)
turtle.colormode(255)

#t.color(0,0,255)

#삼각형 만들기
t.color(0,0,255)
t.up()
t.goto(-150,50)
t.down()
t.circle(70,360,3)

#4각형 만들기
t.color(0,200,0)
t.goto(-150,50)
t.down()
t.circle(50,360,4)

t.color(0,200,0)
t.goto(150,50)
t.down()
t.up()
t.circle(70)

#원형만들기
t.color(255,0,0)
t.goto(150,50)
t.down()
t.up
t.circle(40)

#4각형 만들기
t.color(200,205,10)
t.goto(175,50)
t.down()
t.circle(50,360,4)

#3각형 만들기
t.color(200,255,100)
t.up()
t.goto(-105,-50)
t.down()
t.circle(70,360,3)

