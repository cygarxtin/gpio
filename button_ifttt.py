from gpiozero import LED, Button
from signal import pause
import urllib2

led = LED(17)
button = Button(2)

def ifttt():
	print "done"
	urllib2.urlopen("https://maker.ifttt.com/trigger/button_pressed/with/key/m5WRp6e5B-7j9K2RK-iZLQo9QIG6LD74S9LhCk9CDYY")

button.when_pressed = ifttt

pause()
