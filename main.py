from machine import Pin, I2C
import ssd1306
import time
import urequests
from time import sleep

time.sleep(10)


# ESP32 Pin assignment 
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
 
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

while True:
	try:
		r = urequests.get("http://api.coindesk.com/v1/bpi/currentprice/btc.json")
		rate = '%d' % r.json()['bpi']['USD']['rate_float']
		t = '%s' % r.json()['time']['updated']
		r.close()
	except KeyError:
		rate = "0"
	arr = t.split()	
	oled.fill(0)
	oled.text('BTC-USD',40, 0)
	oled.text(rate,45,23)
	oled.text(arr[3]+' '+ arr[4],18,40)
	oled.text(arr[0]+' '+ arr[1]+' '+ arr[2],20,55)
	oled.show()
	time.sleep(30)

