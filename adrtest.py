from machine import Pin,SoftI2C,Timer
import time
import network
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
#連 wifi
if wlan.isconnected():
    wlan.disconnect()
else:
    wlan.connect('harry0203ch','harry0203ch')
    for i in range(40):
        print('try to connect wifi in {}s'.format(i/2))
        time.sleep(0.5)
        if wlan.isconnected():
            break          
    if wlan.isconnected():
        print('WiFi connection OK!')
        print('Network Config=',wlan.ifconfig())
    else:
        print('WiFi connection Error')
#連 mqtt
        
mqClient0 = MQTTClient('Test2','140.127.220.208')
mqClient0.connect()
i2c = SoftI2C(scl=Pin(5), sda=Pin(2), freq=100000)
scan = i2c.scan()
print('%x'%scan[0])
BH1750_CMD_POWERDOWN = 0x0
BH1750_CMD_POWERON = 0x1
BH1750_CMD_RESET = 0x7
BH1750_CMD_H_RESOLUTION = 0x10
BH1750_CMD_H_RESOLUTION2 = 0x11
BH1750_CMD_L_RESOLUTION = 0x13
BH1750_CMD_ONETIME_H = 0x20
BH1750_CMD_ONETIME_H2 = 0x21
BH1750_CMD_ONETIME_L = 0x23
BH1750_I2C_ADD = 0x23
buf=bytearray(1)
buf[0]= BH1750_CMD_H_RESOLUTION
i2c.writeto(BH1750_I2C_ADD, buf)
#i2c.writeto(BH1750_I2C_ADD, bytearray(BH1750_CMD_H_RESOLUTION))


while True:
    buf = i2c.readfrom(BH1750_I2C_ADD, 0x2)
    data=buf[0]*256+buf[1]
    print(data)
    mqClient0.publish("control messenge",str(data), qos=0)
#    print(buf)
    time.sleep_ms(3000)