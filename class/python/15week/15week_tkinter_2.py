from tkinter import *
import random

def proc() :
    p = random.choice(["냉장고","TV","스마트폰","자동차","노트북"]) #그냥 리스트 배열로 생성해보
    lbl1.configure(text = p)

def c_del():
    lbl1.configure(text="")
    proc() #지우기를 통해서 리스트에 있는 값을 삭제하기

root = Tk()
root.title("버튼")
root.geometry("300x100")

lbl1 = Label(root, text ='당첨 상품은?')
lbl1.pack()
#label을 image로 랜덤 생성하
btn1 = Button(root, text = "추천하기", width=10, height=2, command=proc)
btn1.pack(side = LEFT, padx =30) #place()

btn2 = Button(root, text = "지우기", width=10, height = 2, command=c_del)
btn2.pack(side = LEFT, padx = 5)
root.mainloop()
