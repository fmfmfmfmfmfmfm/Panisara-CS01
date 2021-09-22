from tkinter import *
def clear():
    global expression
    global label_show_cal
    result = "0"
    expression = ""
    label_show_cal.set(result)


def press(number):
    global expression
    global label_show_cal
    expression = expression + number
    label_show_cal.set(expression)

def equal():
    try:
        global expression
        global label_show_cal
        result = str(eval(expression))
        label_show_cal
    except:
        result = "Error"
        expression = ""
    label_show_cal.set(result)

m = Tk()
m.title("F♡rem♡st Calculat♡r")
m.option_add("*font", "consolas 30")
label_show_cal = StringVar()
label_show_cal.set(0)
expression = ""

Label(m, textvariable=label_show_cal, fg="#e411eb", font="consolas 40").grid(row=0 , column=0, columnspan=4, sticky="news")
Button(m, text="clear", command = clear, bg="#fae2ff", width=("3")).grid(row=1 , column=0, columnspan=3, sticky="news")
Button(m, text="/", command=lambda: press("/"), bg="#f7d0ff", width=("3")).grid(row=1 , column=3, sticky="news")

Button(m, text="7", command=lambda: press("7"), width=("3")).grid(row=2 , column=0, sticky="news")
Button(m, text="8", command=lambda: press("8"), width=("3")).grid(row=2 , column=1, sticky="news")
Button(m, text="9", command=lambda: press("9"), width=("3")).grid(row=2 , column=2, sticky="news")
Button(m, text="*", command=lambda: press("*"), bg="#f7d0ff", width=("3")).grid(row=2 , column=3, sticky="news")

Button(m, text="4", command=lambda: press("4"), width=("3")).grid(row=3 , column=0, sticky="news")
Button(m, text="5", command=lambda: press("5"), width=("3")).grid(row=3 , column=1, sticky="news")
Button(m, text="6", command=lambda: press("6"), width=("3")).grid(row=3 , column=2, sticky="news")
Button(m, text="-", command=lambda: press("-"), bg="#f7d0ff", width=("3")).grid(row=3 , column=3, sticky="news")

Button(m, text="1", command=lambda: press("1"), width=("3")).grid(row=4 , column=0, sticky="news")
Button(m, text="2", command=lambda: press("2"), width=("3")).grid(row=4 , column=1, sticky="news")
Button(m, text="3", command=lambda: press("3"), width=("3")).grid(row=4 , column=2, sticky="news")
Button(m, text="+", command=lambda: press("+"), bg="#f7d0ff", width=("3")).grid(row=4 , column=3, sticky="news")

Button(m, text="0  ", command=lambda: press("0"), width=("3")).grid(row=5 , column=0, columnspan=2, sticky="news")
Button(m, text=".", command=lambda: press("."), width=("3")).grid(row=5 , column=2, sticky="news")
Button(m, text="=", command=equal, bg="#f7d0ff", width=("3")).grid(row=5 , column=3, sticky="news")

m.mainloop()