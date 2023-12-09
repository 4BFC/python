from tkinter import *
window = Tk() #이전에는 window대신 root를 사용했었다.

#타이틀
window.title('이미지 표시')
#창 크기
window.geometry('1150x700')

#이미지 변수 생성과 저장
#고양이 이미지도 함께 같이 보여주기
dog = PhotoImage(file="dog.gif")
cat = PhotoImage(file="cat.gif")
#레이블 위젯
lbl_dog = Label(window, image = dog)
lbl_cat = Label(window, image = cat)
lbl_dog.place(x = 20, y =20)
lbl_cat.place(x=500, y=20)

window.mainloop()
