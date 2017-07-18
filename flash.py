from gpiozero import LED, Button
from signal import pause
from time import sleep


led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

def dot():
	led.on()
	sleep(0.1)
	led.off()
	sleep(0.1)

def dash():
	led.on()
	sleep(1)
	led.off()
	sleep(1)

def p():
	dot()
	dash()
	dash()
	dot()

def r():
	dot()
	dash()
	dot()
def i():
	dot()
	dot()
def n():
	dash()
	dot()
def c():
	dash()
	dot()
	dash()
	dot()
def e():
	dot()
	
def say_my_name():
	p()
	r()
	i()
	n()
	c()
	e()

button.when_pressed = say_my_name

pause()
