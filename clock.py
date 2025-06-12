from tkinter import*
import time
def times():
    ctime=time.strftime("%H:%M:%S")
    clock.config(text=ctime)
    clock.after(200,times)
cdate=time.strftime("%d/%B/%Y")

app=Tk()
app.geometry("500x250")
app.config(bg="white")
app.wm_iconbitmap("clock.ico")

app.title("Clock")
Label(text="Digital clock",font="times 25 bold",bg="white").pack(pady=10)
clock=Label(font="times 50 bold",bg="white")
clock.pack(pady=25)
Label(text=cdate,font="times 15 bold",bg="white").pack()

times()
app.mainloop()
