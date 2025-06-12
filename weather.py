from tkinter import *
import requests
from PIL import Image,ImageTk
from urllib.request import urlopen
from io import BytesIO
import time

def text():
    q=e.get()
    key="e3206575c1ca44c4882104452242108"
    url="http://api.weatherapi.com/v1/current.json?key="+key+"&q="+q
    aurl="http://api.weatherapi.com/v1/astronomy.json?key="+key+"&q="+q
    data=requests.get(url)
    data=data.json()

    data1=requests.get(aurl)
    data1=data1.json()

    srise['text']=str(data1['astronomy']['astro']['sunrise'])
    sset['text']=str(data1['astronomy']['astro']['sunset'])
    mrise['text']=str(data1['astronomy']['astro']['moonrise'])
    mset['text']=str(data1['astronomy']['astro']['moonset'])

    
    temp['text']=str(data['current']['temp_c'])+chr(176)+" C"
    loc['text']=str(data['location']['localtime'])
    reg['text']=str(data['location']['name'])+", "+str(data['location']['region'])+", "+str(data['location']['country'])
    tempf['text']=str(data['current']['temp_f'])+"F"
    humid['text']=str(data['current']['humidity'])+"%"
    wspeed['text']=str(data['current']['wind_mph'])+" MPH"
    flike['text']="Feels Like " +str(data['current']['feelslike_c'])+chr(176)+" C"
    cloud['text']=str(data['current']['condition']['text'])
    press['text']=str(data['current']['pressure_mb'])+"atm"
    prep['text']=str(data['current']['precip_mm'])+"mm"
    uv['text']=str(data['current']['uv'])
    hi['text']=str(data['current']['heatindex_c'])+chr(176)+" C"
    
    icon="https:"+str(data['current']['condition']['icon'])
    u=urlopen(icon)
    raw_data=u.read()
    u.close()
    im=Image.open(BytesIO(raw_data))
    photo=ImageTk.PhotoImage(im)
    img['image']=photo
    img.image=photo
    
bg1="#497ba7"
bg2="#1c3a54"

app=Tk()
app.title("Weather")
app.geometry('715x550')
app.resizable=False
app.wm_iconbitmap("cloudy.ico")
forecast=PhotoImage(file="weather-forecast.png")
cdate=time.strftime("%d/%B/%Y")


f1=Frame(bg=bg1,pady=20)
f1.pack(fill=Y,side='left')
f2=Frame(bg=bg2)
f2.pack(fill=Y,side='right')
Label(f1,bg=bg1,width=44).grid(column=0,row=0)

reg=Label(f1,text='City, State',bg=bg1,fg="white",font='times 20 bold',width=18)
reg.grid(column=0,row=1,pady=10)
loc=Label(f1,text=cdate,bg=bg1,fg="white",font="times 15 italic")
loc.grid(column=0,row=2,pady=10)
img=Label(f1,bg=bg1,image=forecast,width=80,height=80)
img.grid(column=0,row=3,pady=10)

temp=Label(f1,text="_"+chr(176)+" C",bg=bg1,fg="white",font="times 30 bold")
temp.grid(column=0,row=4,pady=10)

cloud=Label(f1,text="--",bg=bg1,fg="white",font="times 20")
cloud.grid(column=0,row=5,pady=10)

flike=Label(f1,text="Feels Like: _"+chr(176)+" C",bg=bg1,fg="white",font='times 15')
flike.grid(column=0,row=6,pady=10)

f3=Frame(f2,bg="white",padx=10,pady=20)
f3.pack(side="top")
f4=Frame(f2,bg=bg2,padx=8,pady=20)
f4.pack(side="top",fill=X)
Label(f3,text="Enter Location:",fg=bg2,bg="white",font="times 14").grid(column=0,row=0,sticky='w')
e=Entry(f3,font='times 20',width=20,bd=2)
e.grid(column=0,row=1,padx=10)
b=Button(f3,command=text,text="Search",font='times 13',fg='white',bg=bg2,padx=5,pady=5)
b.grid(column=1,row=1)
Label(f4,bg=bg2,width=40).grid(column=0,row=0)

Label(f4,text="Temp(F)",fg='white',bg=bg2,font="times 16").grid(column=0,row=1,pady=10,sticky='w')
Label(f4,text="Humidity",fg='white',bg=bg2,font="times 16").grid(column=0,row=2,pady=10,sticky='w')
Label(f4,text="Wind speed",fg='white',bg=bg2,font="times 16").grid(column=0,row=3,pady=10,sticky='w')
Label(f4,text="Pressure",fg='white',bg=bg2,font="times 16").grid(column=0,row=4,pady=10,sticky='w')
Label(f4,text="Precipitation",fg='white',bg=bg2,font="times 16").grid(column=0,row=5,pady=10,sticky='w')
Label(f4,text="UV Index",fg='white',bg=bg2,font="times 16").grid(column=0,row=6,pady=10,sticky='w')
Label(f4,text="Heat Index",fg='white',bg=bg2,font="times 16").grid(column=0,row=7,pady=10,sticky='w')



tempf=Label(f4,text="--",fg='white',bg=bg2,font="times 16")
tempf.grid(column=1,row=1,pady=10,sticky='e')
humid=Label(f4,text="--",fg='white',bg=bg2,font="times 16")
humid.grid(column=1,row=2,pady=10,sticky='e')
wspeed=Label(f4,text="--",fg='white',bg=bg2,font="times 16")
wspeed.grid(column=1,row=3,pady=10,sticky='e')
press=Label(f4,text="--",fg='white',bg=bg2,font="times 16")
press.grid(column=1,row=4,pady=10,sticky='e')
prep=Label(f4,text="--",fg='white',bg=bg2,font="times 16")
prep.grid(column=1,row=5,pady=10,sticky='e')
uv=Label(f4,text="--",fg='white',bg=bg2,font="times 16")
uv.grid(column=1,row=6,pady=10,sticky='e')
hi=Label(f4,text="--",fg='white',bg=bg2,font="times 16")
hi.grid(column=1,row=7,pady=10,sticky='e')


f5=Frame(f1,bg=bg1,pady=20)
f5.grid(column=0,row=8)

sunrise=PhotoImage(file="sunrise.png")
sunset=PhotoImage(file="sunset.png")
moonset=PhotoImage(file="moonset.png")
moonrise=PhotoImage(file="moonrise.png")

Label(f5,bg=bg1,image=sunrise).grid(row=0,column=0)
srise=Label(f5,bg=bg1,fg='white',text="--")
srise.grid(row=1,column=0,padx=15)
Label(f5,bg=bg1,image=sunset).grid(row=0,column=1)
sset=Label(f5,bg=bg1,fg='white',text="--")
sset.grid(row=1,column=1,padx=15)
Label(f5,bg=bg1,image=moonrise).grid(row=2,column=0)
mrise=Label(f5,bg=bg1,fg='white',text="--")
mrise.grid(row=3,column=0,padx=15)
Label(f5,bg=bg1,image=moonset).grid(row=2,column=1)
mset=Label(f5,bg=bg1,fg='white',text='--')
mset.grid(row=3,column=1,padx=15)




