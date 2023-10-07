from tkinter import *
root = Tk()
root.title("pack() 배치 관리자 예제")
root.geometry("230x120")
lbl_white = Label(root, text = "white", font = "Times 16 bold italic", fg = "white", bg = "black")

#input을 처리하는 event이다.
ent_input = Entry(root, width=22)
lbl_white.pack()
ent_input.pack()
root.mainloop()
