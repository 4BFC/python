from tkinter import *
root = Tk()
root.title('button_test')
root.geometry("300x300")
def command_test() :
    print("This is a cat")

img = PhotoImage(file='cat.gif')
btn = Button(root, image = img, command = command_test)
btn.place(x=50,y=50)
