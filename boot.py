# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
import network
import os
webrepl.start()
nt = network.WLAN(network.STA_IF); nt.active(True)
nt.connect("SSID","PASSWORD");

