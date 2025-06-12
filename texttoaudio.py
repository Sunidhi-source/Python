import random
from tkinter import*
from tkinter import messagebox
import pyttsx3

engine=pyttsx3.init()
engine.setProperty('volume',1.0)

def action():
    f="outputs/sound"+str(random.randint(11,99))+".mp3"
    text=x.get()
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    engine.save_to_file(text,f)
    messagebox.showinfo("Audio saved","file location "+f)
    
    
app=Tk()
app.geometry('400x400+50+50')
app.title('My Apps')
app.resizable(False,False)
Label(text='Enter text to generate Audio',font=12).pack(pady=20)
x=Entry(width=30,font=14)
x.pack()
Button(text='Generate',bg='brown',fg='white',padx=20,pady=10,command=action).pack(pady=20)
app.mainloop()
