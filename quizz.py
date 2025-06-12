from tkinter import*
import requests
import random

cw=0
ncw=0
url='https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=multiple'
r=requests.get(url)
f=r.json()
d=f['results'][0]
q=d['question']
c=d['correct_answer']
opt=d['incorrect_answers']
opt.append(c)
random.shuffle(opt)

    
def ans():
    global q,c,opt
    k=g.get()
    print(k)
    if g==c:
        r['text']='Your Answer is Correct'
        cw+=1
    else:
        r['text']='Incorrect Answer, Correct Answer is:',c
        ncw+=1
    lbl3['text']='Correct Answers:'+str(cw)
    lbl4['text']='Incorrect Answers:'+str(ncw)


root=Tk()
root.config(bg='black')
root.geometry('600x350')
root.title('Quiz')
g=StringVar()


f1=Frame(bg="red", pady=15,)
f1.pack(fill=X)
lbl1=Label(f1,text='Question Of The Day:',bg='red',fg='white',font='times 20').pack()
lbl3=Label(f1,bg='red',fg='white')
lbl3.pack(sticky="w")
lbl4=Label(f1,bg='red',fg='white')
lbl4.pack(sticky="w")

f2=Frame(pady=15,padx=25)
f2.pack(fill=X)
f3=Frame(bg="red", pady=15,)
f3.pack(fill=X)


lbl2=Label(f2,text=q,font='times 15',wraplength=500)
lbl2.grid(row=1,column=0,padx=20,sticky="w")


rb1=Radiobutton(f2,text=opt[0],variable=g,value=opt[0],font='times 12')
rb2=Radiobutton(f2,text=opt[1],variable=g,value=2,font='times 12')
rb3=Radiobutton(f2,text=opt[2],variable=g,value=3,font='times 12')
rb4=Radiobutton(f2,text=opt[3],variable=g,value=4,font='times 12')
rb1.grid(row=2,column=0,padx=5,sticky="w")
rb2.grid(row=3,column=0,padx=5,sticky="w")
rb3.grid(row=4,column=0,padx=5,sticky="w")
rb4.grid(row=5,column=0,padx=5,sticky="w")


b=Button(f3,text='Check',command=ans,font='times 12')
b.pack()

r=Label(f3,bg='red',fg='white')
r.pack()

root.mainloop()
