from gpiozero import LED
from time import sleep

rojo = LED(13)
azul = LED(19)
verde = LED(26)

cverde = 0
crojo = 0
cazul = 0

while True:
	if cverde == 0:
		verde.on()
	if cverde == 1:
		verde.off()
		cverde = cverde+1
	if cverde == 2:
		cverde == 0

	if cazul < 2:
		azul.on()
	if cazul > 2:
		azul.off()

		cazul=cazul+1
	if cazul==4:
		cazul==0

	if crojo < 4:
		rojo.on()
	if crojo > 4:
		rojo.off()
		crojo=crojo+1
	if crojo==8:
		crojo==0

sleep(0.25)
