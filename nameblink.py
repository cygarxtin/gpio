from gpiozero import LED, Button
from signal import pause
from time import sleep

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_pressed = led.off

def dot():
	led.on()
	sleep(0.5)
	led.off()
	sleep(0.5)

def dash():
	led.on()
	sleep(0.5)
	led.off()
	sleep(1)

def c():
	dot()
def y():
	dash()
	dot()
	dash()
	dot()
def g():
	dot()
	dash()

def say_my_name():
	c()
	y()
	g()


button.when_pressed = say_my_name

pause()
