from tkinter import *
root = Tk()
root.title("로그인하기")
root.geometry("300x200")

def convert() :
    f = float(ent_input.get())
    temp = float(5*(f-32)/9)
    lbl_C.configure(text = temp)

#화씨 lbl
#input Ent
#result lbl

lbl_F = Label(root, text = "화씨")
ent_input = Entry(root)
lbl_C = Label(root, text = "섭씨")
btn = Button(root, text = "섭씨로 변환하기", command = convert)

lbl_F.place(x =10, y =10)
ent_input.place(x =50, y =10)
btn.place(x =50, y =40)
lbl_C.place(x =50, y =80)

root.mainloop()
