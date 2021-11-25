
#RangDev. PASSWORD GENERATOR V1.0

from tkinter import *
import random, string

#window tkinter
root = Tk()
root.geometry("400x280")
root.title("RangDev pw generator")

title = StringVar()
label = Label(root, textvariable=title).pack()
title.set("Select the strength of the password:")


def selection():
    global selection
    selection = choice.get()


#pilihan kekuatan (strength) password
choice = IntVar()
R1 = Radiobutton(root, text="POOR", variable=choice, value=1, command=selection).pack(anchor=CENTER)
R2 = Radiobutton(root, text="AVERAGE", variable=choice, value=2, command=selection).pack(anchor=CENTER)
R3 = Radiobutton(root, text="STRONG", variable=choice, value=3, command=selection).pack(anchor=CENTER)
labelchoice = Label(root)
labelchoice.pack()

#Pilihan Panjang password 
lenlabel = StringVar()
lenlabel.set("Password length:")
lentitle = Label(root, textvariable=lenlabel).pack()

val = IntVar()
spinlenght = Spinbox(root, from_=4, to_=24, textvariable=val, width=13).pack()

# Output pw


def callback():
    lsum.config(text=passgen())


# tombol yg bisa dipencet
passgenButton = Button(root, text="Generate Password", bd=5, height=2, command=callback, pady=3, bg='lightblue')
passgenButton.pack()
password = str(callback)

lsum = Label(root, text="")
lsum.pack(side=BOTTOM)

# fungsi
poor= string.ascii_uppercase + string.ascii_lowercase
average= string.ascii_uppercase + string.ascii_lowercase + string.digits
symbols = """`~!@#$%^&*()_-+={}[]\|:;"'<>,.?/"""
advance = poor+ average + symbols

#generate password (ya random lah namanya juga password generator)
def passgen():
    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(average, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))


root.mainloop()
