from tkinter import *
from tkinter import messagebox

#함수 선언
def clickImg(e):
    messagebox.showinfo("동물이름","고양이")

#윈도우 만들기
window = Tk()
window.title('동물사진')
window.geometry('550x550')

#레이블 위젯에 이미지 보여주기
img = PhotoImage(file='cat.gif')
Plbl = Label(window, image = img) #Label에 이미지를 만들어 낼 수 있다.
#이미지를 보여주고 해당 가격 표를 생성할 수 있다.

#레이블 위젯 마우스 이벤트 함수 호출하기
Plbl.bind("<Button>",clickImg)
#Plbl.place(x=20,y=20)
Plbl.pack()

window.mainloop()
