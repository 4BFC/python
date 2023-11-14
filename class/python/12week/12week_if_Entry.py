from tkinter import *
root = Tk()
root.title("윈도우 창 만들기")
#geometry는 윈도우 창 크기를 결정 짓는 명령어이다.
root.geometry("230x120")

def pass_check():
    score = int(ent.get())

    if score >= 70:
        #lbl_status.configure(text = "합격")
        lbl_img.configure(text = "합격")
        lbl_img = Label(root, text = "합격")#image = photo1
        lbl_img.place(x=100, y=30)
    else :
        lbl_status.configure(text="불합격")
        lbl_img = Label(root, image = photo2)
        lbl_img.place(x=100, y=30)

photo1 = PhotoImage(file="smile.png")
photo2 = PhotoImage(file="try.png")

lbl = Label(root, text = "정수")
ent = Entry(root, width= 20)
btn = Button(root, text = "확인", command = pass_check)
lbl_status = Label(root, text = "합격여부")

lbl.place(x = 10, y = 10)
ent.place(x = 50, y = 10)
btn.place(x = 50, y = 40)
lbl_status.place(x = 50, y = 80)

#위치를 배치하려면 pack으로 지정하면 안된다.
#lbl.pack()
#ent.pack()
#btn.pack()
#lbl_status.pack()
root.mainloop()

#https://076923.github.io/posts/Python-tkinter-12/
