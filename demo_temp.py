from tkinter import *
from tkinter import ttk

import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=70489dd90f0a859fd3ea133708e822ec").json()
    w_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title(" Weather System ")
win.config(bg= "gray")
win.geometry("550x540")

name_label = Label(win, text="Weather App System",
                   font=("Time New Roman", 35, "bold"))
name_label.place(x=25,y=50,height=50,width=500)

city_name = StringVar()
list_name = ['Kathmandu','Damak','Illam','Itahari', 'Kageshwori Manohara', 'Kirtipur', 'Gokarneshwor', 'Chandragiri', 'Tokha', 'Tarkeshwor', 'Dakchinkali', 'Nagarjun', 'Budhanilkantha', 'Shankharapur']
com = ttk.Combobox(win, text="Weather App System",values=list_name,
                   font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=40,y=130,width=450)

w_label = Label(win, text="Weather Climate",
                   font=("Time New Roman", 15))
w_label.place(x=27,y=260,height=40,width=200)

w_label1 = Label(win, text="",
                   font=("Time New Roman", 15))
w_label1.place(x=250,y=260,height=40,width=200)

wd_label = Label(win, text="Weather Description",
                   font=("Time New Roman", 15))
wd_label.place(x=25,y=320,height=40,width=200)

wd_label1 = Label(win, text="",
                   font=("Time New Roman", 15))
wd_label1.place(x=250,y=320,height=40,width=200)

temp_label = Label(win, text="Temperature",
                   font=("Time New Roman", 15))
temp_label.place(x=25,y=380,height=40,width=200)

temp_label1 = Label(win, text="",
                   font=("Time New Roman", 15))
temp_label1.place(x=250,y=380,height=40,width=200)

per_label = Label(win, text="Pressure",
                   font=("Time New Roman", 15))
per_label.place(x=25,y=440,height=40,width=200)

per_label1 = Label(win, text="",
                   font=("Time New Roman", 15))
per_label1.place(x=250,y=440,height=40,width=200)


submit_button = Button(win, text="Done",
                   font=("Time New Roman", 20, "bold"), command=data_get)
submit_button.place(y=190, height=40, width=90,x=200)


win.mainloop()