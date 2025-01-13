# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
import network
#webrepl.start()
gc.collect()
wlan = network.WLAN(network.STA_IF)
ap = network.WLAN(network.AP_IF)
ap.active(False)
wlan.active(True)
wlan.scan()
wlan.connect('HTW_H106_Rechnernetze', 'rnFIW625')
wlan.isconnected()
wlan.ifconfig()

import dht
d = dht.DHT22(machine.Pin(4))
d.measure()
d.temperature()
d.humidity()