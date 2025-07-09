from tkinter import *

def click(event):
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        try:
            result = eval(scvalue.get())
            scvalue.set(str(result))
            screen.update()
        except Exception:
            scvalue.set("Error")
            screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("500x600") 
root.title("Calculator")
root.focus_set() 

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 25 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Row 1
f = Frame(root, bg="grey")
b = Button(f, text="9", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)
f.pack()

# Row 2
f = Frame(root, bg="grey")
b = Button(f, text="6", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=24, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)
f.pack()

# Row 3
f = Frame(root, bg="grey")
b = Button(f, text="3", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=24, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)
f.pack()

# Row 4
f = Frame(root, bg="grey")
b = Button(f, text="0", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=18, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=20, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=24, pady=20, font="lucida 25 bold")
b.pack(side=LEFT, padx=15, pady=10, expand=True)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()
