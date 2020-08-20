from tkinter import *
from PIL import Image,ImageTk
from functools import partial
import random
from win32com.client import Dispatch
import tkinter.messagebox as ms
swg = Tk()
def speak(st):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(st)
def new():
    global your, comp,gameover,l1
    your = 0
    comp = 0
    gameover = False
    img = Image.open("Images/blank.png").resize((200, 200), Image.ANTIALIAS)
    im = ImageTk.PhotoImage(img)
    can.image = im
    can.create_image(114, 114, image=im)
    can1 = Canvas(swg, width=250, height=250)
    img1 = Image.open("Images/blank.png").resize((200, 200), Image.ANTIALIAS)
    im1 = ImageTk.PhotoImage(img1)
    can1.image = im1
    can1.create_image(114, 114, image=im1)
    can.grid(column=0)
    can1.grid(row=1, column=10, padx=80)
    ly["text"] = "Your Score:" + str(your)
    lc["text"] = "Computer Score:" + str(comp)
    l1["text"] = ""
def exit():
    mess = ms.askquestion("Exit","Do you want to Exit?")
    if(mess == "yes"):
        swg.destroy()
    else:
        pass
def game(st):
    global your,comp,choice,gameover
    if(gameover==False):
        you = st
        compu = random.choice(choice)
        img = Image.open("Images/" + st + ".png").resize((200, 200), Image.ANTIALIAS)
        im = ImageTk.PhotoImage(img)
        can.image = im
        can.create_image(114, 114, image=im)
        can1 = Canvas(swg, width=250, height=250)
        img1 = Image.open("Images/" + compu + ".png").resize((200, 200), Image.ANTIALIAS)
        im1 = ImageTk.PhotoImage(img1)
        can1.image = im1
        can1.create_image(114, 114, image=im1)
        can.grid(column=0)
        can1.grid(row=1, column=10,padx=80)
        if ((you == "snake" and compu == "water") or (you == "water" and compu == "gun") or (
                you == "gun" and compu == "snake")):
            your = your + 1
            speak("You Get a Point")
        elif ((compu == "snake" and you == "water") or (compu == "water" and you == "gun") or (
                compu == "gun" and you == "snake")):
            comp = comp + 1
            speak("Computer Get a Point")
        else:
            speak("It's a Tie")
        ly["text"] = "Your Score:" + str(your)
        ly.grid(row=21, column=0, pady=35)
        lc["text"] = "Computer Score:" + str(comp)
        lc.grid(row=21, column=10)
        if (your == 10):
            l1["text"]="You Won"
            l1.grid()
            speak("You Won")
            gameover=True
        elif (comp == 10):
            l1["text"] = "Computer Won"
            l1.grid()
            speak("Computer Won")
            gameover=True

swg.geometry("1100x700")
swg.title("Snake-Water-Gun")
swg.wm_iconbitmap("Images/clipart3028630_wks_icon.ico")
your=0
comp=0
choice = ["snake","water","gun"]
gameover=False
Label(text="You",font="lucida 23 bold").grid()
Label(text="Computer",font="lucida 23 bold").grid(row=0,column=10)
can = Canvas(swg,width=250,height=250)
img = Image.open("Images/blank.png").resize((200, 200), Image.ANTIALIAS)
im = ImageTk.PhotoImage(img)
can.image = im
can.create_image(114, 114, image=im)
can1 = Canvas(swg, width=250, height=250)
img1 = Image.open("Images/blank.png").resize((200, 200), Image.ANTIALIAS)
im1 = ImageTk.PhotoImage(img1)
can1.image = im1
can1.create_image(114, 114, image=im1)
can.grid(column=0)
can1.grid(row=1, column=10,padx=80)
f1=Frame(width=7)
f1.grid(row=22,column=0)
but1 = Button(f1,text="Snake",width=14,command=partial(game,"snake"))
but1.grid(row=2,column=1,padx=10)
but2 = Button(f1,text="Water",width=14,command=partial(game,"water"))
but2.grid(row=2,column=2,padx=10)
but3 = Button(f1,text="Gun",width=14,command=partial(game,"gun"))
but3.grid(row=2,column=3,padx=10)
ly = Label(text="Your Score:"+str(your),font="lucida 20 bold")
ly.grid(row=21,column=0,pady=35)
lc = Label(text="Computer Score:"+str(comp),font="lucida 20 bold")
lc.grid(row=21,column=10)
f2 = Frame()
f2.grid(row=25,column=9,padx=50,pady=115)
l1 = Label(f2, text="You Won", fg="green", font="lucida 30 bold")
men = Menu()
men1 = Menu(men,tearoff=0)
men1.add_command(label="New Game",command=new)
men1.add_command(label="Exit",command=exit)
men.add_cascade(label="New",menu=men1)
swg.config(menu=men)
swg.mainloop()
