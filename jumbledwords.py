from tkinter import*
import random
from tkinter.messagebox import*

clr1="Teal"
clr2="White"
clr3="Orange"
cvalue=wvalue=0
anslist=["apple","mango","kiwi","orange","apricot","avacado","grapes"]
wordlist=[''.join(random.sample(x,len(x))) for x in anslist]
print(wordlist)
num=random.randrange(0,len(anslist),1)

def default():
    global wordlist,anslist,num,cvalue,wvalue
    w.config(text="Word is : "+wordlist[num])
    cv.config(text=cvalue)
    wv.config(text=wvalue)
def wordTest():
    global wordlist,anslist,num,cvalue,wvalue
    if(e1.get()==''):
        showwarning("Empty","Type Something")
        reset()
    elif(e1.get()==anslist[num]):
        cvalue+=1
        cv.config(text=cvalue)
        showinfo("Sucess","Correct Answer")
        if (cvalue==5):
            showinfo("Finish","Thanks For Playing")
            win.destroy()
        else:
            reset()
    else:
        wvalue+=1
        wv.config(text=wvalue)
        showerror("Oops","This is Incorrect Try Again")
        e1.delete(0,END)
        
   
def reset():
    global wordlist
    num=random.randrange(0,len(anslist),1)
    w.config(text="Word is"+anslist[num])
    e1.delete(0,END)
def whint():
    global anslist
    f=anslist[num][0]
    l=anslist[num][-1]
    showinfo("Hint",f+"____"+l)


win=Tk()
win.title("Jumbled Words Game")
win.geometry('400x400')
win.config(bg=clr2)

sf=Frame(pady=5,bg=clr1)
sf.pack(side='top',fill='x')
Label(sf,bg=clr1,fg=clr2,text="Correct").pack(side="left",anchor="nw")
cv=Label(sf,bg=clr1,fg=clr2)
cv.pack(side="left",anchor="nw")
Label(sf,bg=clr1,fg=clr2,text="Wrong").pack(side="left",anchor="nw")
wv=Label(sf,bg=clr1,fg=clr2)
wv.pack(side="left",anchor="nw")

wf=Frame(pady=30,bg=clr1)
wf.pack(side="top",fill="x")

w=Label(wf,padx=5,pady=5,bg=clr1,fg=clr2)
w.pack()

Label(wf,padx=5,pady=5,bg=clr1,fg=clr2,text="Enter Correct Word").pack()
e1=Entry(wf)
e1.pack()


f=Frame(width=200,bg=clr2,pady=20)
f.pack(anchor='center')

btn=Button(f,text="Check",bg=clr3,fg=clr1,command=wordTest)
btn.pack(side='left')

Button(f,text="Reset",bg=clr3,fg=clr1,command=reset).pack(side='left')
Button(f,text="Hint",bg=clr3,fg=clr1,command=whint).pack(side='left')
Button(f,text="End game",bg=clr3,fg=clr1,command=win.destroy).pack(side='left')

default()
