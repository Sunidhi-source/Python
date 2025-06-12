from tkinter import *
import requests

bg1="#D5E4EA"
l=('INR','USD','EUR','AED','CAD','AUD','GBP')

def check():
    x=f.get()
    y=t.get()
    a=m.get()
    key="b02d684582a12e76b06c4b7e"
    url=f"https://v6.exchangerate-api.com/v6/{key}/pair/{x}/{y}/{a}"
    data=requests.get(url)
    data=data.json()
    rate['text']='Currency Rate: ' +str(data['conversion_rate'])
    res['text']='Total Amount: ' +str(data['conversion_result'])
    
    
app=Tk()
app.geometry("400x400")
app.config(bg=bg1)
app.title("Currency Converter")
arrow=PhotoImage(file='right-arrow.png')


Label(text="Currency Converter",bg=bg1,fg="black",font="times 25 bold").grid(row=0,column=0,columnspan=3,padx=50,pady=20)

Label(text="From:",fg="black",bg=bg1,font="times 18").grid(row=1,column=0)
Label(image=arrow,bg=bg1,font="times 18").grid(row=1,column=1)
Label(text="To:",fg="black",bg=bg1,font="times 18").grid(row=1,column=2)

f=StringVar()
f.set("Select Currency")
s=OptionMenu(app,f,*l)
s.grid(row=2,column=0)

t=StringVar()
t.set("Select Currency")
q=OptionMenu(app,t,*l)
q.grid(row=2,column=2)

m=IntVar()
Label(text="Amount:",fg="black",bg=bg1,font='times 18').grid(row=3,column=0,padx=10,pady=20)
r=Spinbox(from_=1,to_=5000,font="times 12",textvariable=m)
r.grid(row=3,column=1,padx=10,pady=10,columnspan=3)

b=Button(text="Check",command=check,bg="black",fg='white',font='times 15')
b.grid(row=4,column=0,columnspan=3)

rate=Label(bg=bg1,fg="black",font='times 14')
rate.grid(column=0,row=5,columnspan=3,pady=5)

res=Label(bg=bg1,fg="black",font='times 14')
res.grid(column=0,row=6,columnspan=3)

