# This file is executed on every boot (including wake-boot from deepsleep)
import network
import dht
import machine
from umqttsimple import MQTTClient
import time
import utime
    
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('HTW_H106_Rechnernetze', 'rnFIW625')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ipconfig('addr4'))
    
do_connect()

d = dht.DHT22(machine.Pin(2))
d.measure()
d.temperature()
d.humidity()

client = MQTTClient("ProIT_Rohanclient", "broker.f4.htw-berlin.de")

client.connect()
while True:
    time.sleep(10)
    
    # Get the current timestamp
    current_time = utime.localtime()  # Returns (year, month, mday, hour, minute, second, weekday, yearday)
    timestamp = "{}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(*current_time[:6])
    
    print("Measuring Temperature and Humidity")
    d.measure()
#     client.publish("HTW_IoTM2425/Rohan/temp", b"%s" % d.temperature())
    client.publish(
    "HTW_IoTM2425/Rohan/temp",
    '{"value": b"%s", "timestamp": "%s"}' % (d.temperature, timestamp)
    )
#     client.publish("HTW_IoTM2425/Rohan/humi", b"%s" % d.humidity())
    client.publish(
    "HTW_IoTM2425/Rohan/humi",
    '{"value": b"%s", "timestamp": "%s"}' % (d.humidity, timestamp)
    )


