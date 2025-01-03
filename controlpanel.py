import tkinter as tk
import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("140.127.220.208", 1883)


def open():
    client.publish("control messenge", "open")
    print("test, open.")
    button_open['bg']  = 'orange'
    button_open['state'] = 'disabled'
    button_close['bg'] = '#FFFFFF'
    button_close['state'] = 'active'

def close():
    client.publish("control messenge", "close")
    print("test, close.")
    button_open['bg']  = '#FFFFFF'
    button_open['state'] = 'active'
    button_close['bg'] = 'orange'
    button_close['state'] = 'disabled'

window = tk.Tk()
window.title('controller')
window.geometry("200x200+250+150")

# 建立按鈕
button_open = tk.Button(window,text = '開啟',command = open,width='20',height='3') 

button_close = tk.Button(window,text = '關閉',command = close,width='20',height='3')

button_open.pack()
button_close.pack()

window.mainloop()