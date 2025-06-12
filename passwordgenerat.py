from tkinter import *
import random
letters=[chr(x)for x in range(65,91)]+[chr(x)for x in range(97,123)]
numbers=[str(x)for x in range(0,9)]
symbols=['@','*','#','$','&','%']

def text():
    p=int(l.get())
    sy=int(s.get())
    di=int(d.get())
    pw=[]
    for x in range(0,sy):
        pw.append(random.choice(symbols))
    for x in range(0,di):
        pw.append(random.choice(numbers))
    for x in range(0,p-(sy+di)):
        pw.append(random.choice(letters))
    np=""
    random.shuffle(pw)
    np=np.join(pw)
    print(np)
    lb['text']="The password is:",np
    
app=Tk()
app.geometry("500x250")
Label(text="Welcome to the Password Generator",fg="brown",font="times 12").grid(row=0,column=0,padx=5,pady=5,columnspan=2)
Label(text="Enter your requirements",fg="black",font="times 12").grid(row=1,column=0,padx=5,pady=5,columnspan=2)

Label(text="Password Length:",fg="black",font="times 10").grid(row=2,column=0)
l=Spinbox(from_=1,to_=9)
l.grid(row=2,column=1)

Label(text="No. of Symbols:",fg="black",font="times 10").grid(row=3,column=0)
s=Spinbox(from_=1,to_=9)
s.grid(row=3,column=1)

Label(text="No. of digits:",fg="black",font="times 10").grid(row=4,column=0)
d=Spinbox(from_=1,to_=9)
d.grid(row=4,column=1)

b=Button(text="Generate",command=text,fg="black",font="times 12")
b.grid(row=5,column=0)

lb=Label()
lb.grid(row=6,column=0)

