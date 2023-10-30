#tkinter 연결하기
from tkinter import *
root = Tk()
root.title("로그인하기")
root.geometry("200x100")

#콘솔에 '로그인입니다.'함수구현
def Login():
    print("로그인입니다")

## 위젯 생성 구역
#아이디 Lable
lbl_ID = Label(root, text = "아이디(ID)")
#비밀번호 Lable
lbl_PW = Label(root, text = "비밀번호(PW)")
#아이디 input
ent_ID = Entry(root, width=27)
#비밀번호 input
ent_PW = Entry(root, width=27)
#login 버튼 
btn_login = Button(root, text = "로그인하기", fg = "white", bg = "black", command=Login)

##pack함수 구역
lbl_ID.pack()
ent_ID.pack()
lbl_PW.pack()
ent_PW.pack()
btn_login.pack(side=BOTTOM)

root.mainloop()
