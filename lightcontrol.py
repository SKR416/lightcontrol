from machine import Pin
import time
from umqtt.simple import MQTTClient as umqtt
import network
def get_msg(topic,msg):
    global  control
    global count
    msg1=str(msg).replace('b','').replace("'",'')
    
    if msg1=='on':
        control=True
        p2.value(1)
        count=0
    elif msg1=='off':
        control=True
        p2.value(0)
        count=0
    
    if control==True:
        count+=0.5
        if count>4:
            control=False
            count=0
    else:
        msg1=int(msg)
        if msg1<=20:
            p2.value(1)
        else:
            p2.value(0)
    return msg1

p2=Pin(2,Pin.OUT)
control=False;
count=0;
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if wlan.isconnected():
    wlan.disconnect()
else:
    wlan.connect('harry0203ch','harry0203ch')
    for i in range(20):
        print('try to connect wifi in {}s'.format(i/2))
        time.sleep(0.5)
        if wlan.isconnected():
            break          
    if wlan.isconnected():
        print('WiFi connection OK!')
        print('Network Config=',wlan.ifconfig())
    else:
        print('WiFi connection Error') 
    
mqClient0 = umqtt('xiang','140.127.220.208')
mqClient0.connect()
mqClient0.set_callback(get_msg)
mqClient0.subscribe('control messenge')

while True:
    
    msg=mqClient0.check_msg()
    print(control)
    print(count)
    time.sleep(0.5)