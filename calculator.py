from tkinter import*
clr='teal'

def calcvalue(event):
    b=event.widget.cget('text')
    if b=='=':
        try:
            txt.set(eval(txt.get()))
        except:
            txt.set("Invalid Inputs")
    elif b=='C':
        txt.set("")
    else:
        t=txt.get()+b
        txt.set(t)
        
        
win=Tk()
win.title("Calc App")
win.geometry("325x340+200+100")
win.config(bg=clr)

x=0
btn=['C','=','/','*','9','8','7','+','6','5','4','-','3','2','1','0']

txt=StringVar()
Entry(win,textvariable=txt,font="times 20 bold").pack(fill=X,padx=5,pady=15)

for row in range(4):
    f=Frame(win,bg='white')
    for cols in range(4):
        b=Button(f,text=btn[x],height=1,width=3,font='times 15 bold',bg='black',fg='white')
        b.pack(side='left',padx=9,pady=8)
        b.bind("<Button-1>",calcvalue)
        x+=1
    f.pack(padx=4)

win.mainloop()
