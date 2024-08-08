from gpiozero import LED
from gpiozero import Button

led = LED(19)
button = Button(12)

while True:
	if button.is_pressed:
		led.on()
	else:
		led.off()

pause()
