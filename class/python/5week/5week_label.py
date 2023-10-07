from tkinter import *
root = Tk()
root.title("윈도우 창 만들기")
#geometry는 윈도우 창 크기를 결정 짓는 명령어이다.
root.geometry("230x120")

##label을 결정 짓는 부분이다.
lbl_red = Label(root, text = "red")
lbl_green = Label(root, text = "green")
lbl_white = Label(root, text = "white", font="Times 20 bold italic", fg = "white", bg = "black")

#pack이란 무엇이고 어떤 역할을 하는 것인가.
lbl_red.pack()
lbl_green.pack()
lbl_white.pack()
root.mainloop()
