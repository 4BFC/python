#root 만들기
from tkinter import *
root = Tk()
root.title("커피 주문받기")
root.geometry("580x350")


#금액 계산하는 함수
def Order():
    Coffee1_Tprice = coffee_price[0] * int(ent_Coffee1_num.get())
    Coffee2_Tprice = coffee_price[1] * int(ent_Coffee2_num.get())
    Coffee3_Tprice = coffee_price[2] * int(ent_Coffee3_num.get())
    Cooki_Tprice = coffee_price[3] * int(ent_Cooki_num.get())

    #총금액 계산
    Total_price = Coffee1_Tprice + Coffee2_Tprice + Coffee3_Tprice + Cooki_Tprice
    #평균 계산(반올림)
    Average = int(Total_price / int(ent_Person_num.get()))

    #총금액 출력하기
    lbl_Total_Price.configure(text = "주문한 총금액은 " + str(Total_price) + "원입니다.")
    #평균 출력하기
    lbl_Average.configure(text = "1인당 지불한 금액은 " + str(Average) + "원입니다.")

#커피 종류 리스트 만들기
coffee_name = ['아메리카노','카페라떼','카페모카','쿠키']
coffee_price = [2000,3000,3500,5000]

#위젯 생성하기
#제목
lbl_name = Label(root, text = "커피 종류")
lbl_price = Label(root, text = "커피 가격")
lbl_num = Label(root, text = "주문 수량")

#아메리카노
lbl_Coffee1_name = Label(root, text = coffee_name[0])
lbl_Coffee1_price = Label(root, text = coffee_price[0])
ent_Coffee1_num = Entry(root)

#카페라떼 
lbl_Coffee2_name = Label(root, text = coffee_name[1])
lbl_Coffee2_price = Label(root, text = coffee_price[1])
ent_Coffee2_num = Entry(root)

#카페모카
lbl_Coffee3_name = Label(root, text = coffee_name[2])
lbl_Coffee3_price = Label(root, text = coffee_price[2])
ent_Coffee3_num = Entry(root)

#쿠키 
lbl_Cooki_name = Label(root, text = coffee_name[3])
lbl_Cooki_price = Label(root, text = coffee_price[3])
ent_Cooki_num = Entry(root)

#인원수
lbl_person = Label(root, text = "인원 수 :")
ent_Person_num = Entry(root)
lbl_Total_Price =  Label(root, text = "Total_Price :")
lbl_Average = Label(root, text = "Average_Price :")
#최종 출력


paybtn = Button(root, text ="금액계산", command = Order)

#위젯 배치하기
#제목
lbl_name.place(x=60, y=10)
lbl_price.place(x=240, y=10)
lbl_num.place(x=400, y= 10)

#아메리카노 
lbl_Coffee1_name.place(x=60, y=40)
lbl_Coffee1_price.place(x=200, y=40)
ent_Coffee1_num.place(x=360, y=40)

#카페라때
lbl_Coffee2_name.place(x=60, y=60)
lbl_Coffee2_price.place(x=200, y=60)
ent_Coffee2_num.place(x=360, y=60)

#카페모카  
lbl_Coffee3_name.place(x=60, y=80)
lbl_Coffee3_price.place(x=200, y=80)
ent_Coffee3_num.place(x=360, y=80)

#쿠키
lbl_Cooki_name.place(x=60, y=100)
lbl_Cooki_price.place(x=200, y=100)
ent_Cooki_num.place(x=360, y=100)

#인원수
lbl_person.place(x=60,y=120)
ent_Person_num.place(x=200, y=120)
lbl_Total_Price.place(x=200, y=160)
lbl_Average.place(x=200, y=200)

#버튼
paybtn.place(x=100, y=140)
root.mainloop()
