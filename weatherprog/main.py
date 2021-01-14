import eel
import pyowm

#owm = pyowm.OWM("2a2d8171f2fe87038519f3f9d43747e8")
city = "New York"


owm = pyowm.OWM("2a2d8171f2fe87038519f3f9d43747e8")
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather

temp = w.temperature('celsius')['temp']

print("В городе " + city + " сейчас " + str(temp) + " градусов!")

#eel.init("web")
#eel.start("main.html", size=(700, 700))