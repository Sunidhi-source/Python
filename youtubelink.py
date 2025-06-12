
from tkinter import*
from tkinter import messagebox
from pytube import YouTube

def action():
    try:
        text=x.get()
        yt=YouTube(text)
        yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download()
        messagebox.showinfo("Video saved")
    except:
        messagebox.showinfo("Some error occured")


app=Tk()
app.geometry('400x400+50+50')
app.title('My Apps')
app.resizable(False,False)
Label(text='Paste the link',font=12).pack(pady=20)
x=Entry(width=30,font=14)
x.pack()
Button(text='Download',bg='brown',fg='white',padx=20,pady=10,command=action).pack(pady=20)
app.mainloop()

