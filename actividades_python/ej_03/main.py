from gpiozero import LED
from gpiozero import Buzzer

rojo = LED(19)
verde = LED(26)
azul = LED(13)
bz = Buzzer(22)

while True:
	entrada = input("prompt: ")
	if entrada == "buzz on":
		bz.on()
	if entrada == "buzz off":
		bz.off()
	if entrada == "rgb red":
		rojo.toggle()
	if entrada == "rgb green":
		verde.toggle()
	if entrada == "rgb blue":
		blue.toggle()

