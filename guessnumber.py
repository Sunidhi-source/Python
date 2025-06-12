from tkinter import*
import random
def text():
    r=random.randint(1,10)
    b=int(a.get())
    if r==b:
        l['text']= 'You won!'
    else:
        l['text']= 'You lost!'
    user['text']='User choice : '+str(b)
    com['text']='Comp choice : '+str(r)
      
app=Tk()
app.config(bg='white')
Label(text="Guess the Number",fg='red',bg='white',font=20).grid(row=0,column=1)
Label(text="(from 1-10)",fg='black',bg='white',font=10).grid(row=1,column=1)

a=Spinbox(from_=1,to_=10,font=15)
a.grid(row=2,column=1,padx=5,pady=5)

s=Button(text="Check",command=text)
s.grid(row=3,column=1)

l=Label(bg='white',fg='red',font=20)
l.grid(row=4,column=1)

com=Label(fg='black',bg='white',font=10)
com.grid(row=5,column=1)
user=Label(fg='black',bg='white',font=10)
user.grid(row=6,column=1)

app.mainloop()
