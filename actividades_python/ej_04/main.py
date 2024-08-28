import gpiozero
import time
import math
import ADS1x15

ads = ADS1x15.ADS1115(1)
ads.setMode(ADS.MODE_SINGLE)
ads.setGain(ADS.PGA_4_096V)
conv = ads.toVoltage()
blue = PWMLED(26)
green = PWMLED(13)

# Declaro las variables a utilizar para el cálculo de la diferencia en temp.

VCC = 3.3       # VCC = Fuente
VRTH = 0        # VRTH = Voltaje sobre el termistor(TH)
RTH = 0         # RTH = Resistencia del TH
T = 0           # T = Temperatura base medida
R = 10000       # R = Resistencia del divisor de tensión con el TH
b = 3977        # b = Factor de ganancia del termistor

while True:
    potval = ads.readADC(3)     # Leo las entradas analógicas 1 y 3, que son el
    thval = ads.readADC(1)      # pote y TH respectivamente

    potvalV = potval*conv   # Convierto los valores del ADC a voltaje utilizando
    thvalV = thval*conv     # el valor de referencia toVoltage 'conv'

    # Calculo la temperatura

    VRTH = (3.3*thvalV)/4095
    RTH = R((VCC/VRTH)-1)
    T = b/(math.log10(RTH/R)+(b/298.0))
    T = T - 273.15

    # Determino las condiciones de encendido e intensidad de brillo de los LEDs

    if (potvalV>thvalV):
        blue.value = (potvalV - thvalV)*0.2 
        if (blue.value>1):
            blue.value = 1
        time.sleep(1)
    
        # Si el valor establecido en el pote es MAYOR al del TH, se encenderá
        # el LED azul, que alcanzará su brillo máximo cuando haya una
        # diferencia de 5 o más grados.

    elif (potvalV<thvalV):
        green.value = (thvalV - potvalV)*0.2
        if (green.value>1):
            green.value = 1
        time.sleep(1)

        # En el caso adverso, si el valor del pote es MENOR al del TH, se
        # encenderá el LED verde, que alcanzará su brillo máximo cuando haya una
        # diferencia de 5 o más grados.

    else:
        blue.value = 0
        green.value = 0
        time.sleep(1)

        # En el caso de que la temperatura en el pote y la medida por el TH
        # sean iguales, los LEDs permanecerán apagados.

    # Muestra en pantalla los valores a conocer por la actividad

    print("Valor del termistor = {0:.3f}V".format(thvalV))
    print("Temperatura establecida en el potenciómetro = {0:.3f}V".format(potvalV))
    print("Temperatura medida por el termistor = {0:.3f}°C".format(T))
time.sleep(1)
