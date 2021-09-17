from tkinter import *

root = Tk()
root.title("First GUI")
myText = Label(text="MyName is",fg="#481fff",font=50).grid(row=0,column=0)
myText = Label(text="Panisara",fg="#ff66f6",font=50).grid(row=1,column=1)
myText = Label(text="Mungmek",fg="#aa4fff",font=50).grid(row=2,column=2)
myText = Label(text="♡",fg="#79ff1f",font=50).grid(row=3,column=3)
root.geometry("500x500")
root.mainloop()