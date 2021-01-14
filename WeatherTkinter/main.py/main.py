from tkinter import *
from tkinter import messagebox
import requests

root = Tk()

def get_weather():
    city = cityField.get()

    key = '2a2d8171f2fe87038519f3f9d43747e8'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':key, 'q': city, 'units': 'imperial'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}: {round(((5/9)*(float(weather["main"]["temp"])-32)), 2)} градусов'


root['bg'] = '#fafafa'
root.title('Погодное приложение')
root.geometry('300x250')

root.resizable(width=False, height=False)

frame_top = Frame(root,bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_botton = Frame(root, bg='#ffb700', bd=5)
frame_botton.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.2)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()

info = Label(frame_botton, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

root.mainloop()