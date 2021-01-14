import os
import time

print("Програма для выключения ПК!")
print("Введите время через которое нужно выключить компьютер в минутах:")

time_m = int(input())
time_s = time_m *60
time_now = time.localtime()
time_off = time.localtime(time.time() + time_s)
tString_now = time.strftime("%d/%m/%Y  %H:%M:%S", time_now)
tString_off = time.strftime("%d/%m/%Y  %H:%M:%S", time_off)

print()
print("Компьютер выключиться через ", time_m," минут!")
print("Текущая дата и время: ", tString_now)
print("Ваш компьютер будет выключен: ", tString_off)

time.sleep(time_s)
os.startfile("E:\Project\Off_PC\shutdown.bat")  # Выключение ПК через bat-файл
