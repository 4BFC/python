from tkinter import *
root = Tk()
root.title("로그인하기")
root.geometry("200x100")

def Login():
    print("로그인입니다")

lbl_ID = Label(root, text = "아이디(ID)")
lbl_PW = Label(root, text = "비밀번호(PW)")
ent_ID = Entry(root, width=27)
ent_PW = Entry(root, width=27)
btn_login = Button(root, text = "로그인하기", fg = "white", bg = "black", command=Login)

lbl_ID.pack()
ent_ID.pack()
lbl_PW.pack()
ent_PW.pack()
btn_login.pack(side=BOTTOM)

root.mainloop()
