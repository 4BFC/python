from tkinter import *
root = Tk()
root.title("image 조작하기")
root.geometry("300x250")

def add() :
    #이렇게 직접 받아오는 것 밖에 없다.
    a = int(a_ent.get())
    b = int(b_ent.get())
    result = a+b
    lbl.configure(text = f"result : {a} + {b} = {result}")
    return a+b

def check():
    a_result = a_ent.get()
    b_result = b_ent.get()
    print(a_result)
    print(b_result)
    lbl.configure(text = f"result : {a_result}, {b_result}")
    
#위젯 설정     
a_ent = Entry(root, width = 20)
b_ent = Entry(root, width = 20)
btn = Button(root,text="add",command = add)
lbl = Label(root, text = "result")

a_ent.pack()
b_ent.pack()
btn.pack()
lbl.pack()

root.mainloop()
