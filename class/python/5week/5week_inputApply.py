from tkinter import *
root = Tk()
root.title("버튼과 이벤트")
root.geometry("230x120")

#함수 구현
def proc():
    print("Hello!!")

#command역할은 무엇인가.
btn = Button(root, text = "인사하기", command=proc)
#side는 무엇인가.
btn.pack(side=BOTTOM)
root.mainloop()
