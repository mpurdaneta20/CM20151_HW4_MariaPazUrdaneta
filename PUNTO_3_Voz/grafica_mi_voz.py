# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

#PUNTO 3B
from pylab import *

from scipy.io import wavfile

#Se abre el archivo y se obtiene la frecuencia y la señal del sonido generado
frecuencia, senal = wavfile.read('nombre.wav')

#Genera el el array con la señal de la grabacion
print senal 

#Genera un rango de frecuencias entre -1 y 1
senal=senal/(2.**15)

#Halla duracion de la grabacion
frec=senal.shape[0]/float(frecuencia)
print frec

#Se obtine el tiempo de grabacion en el intervalo de tiempo de 0 al total de observaciones (frames)
timeArray = arange(0,senal.shape[0], 1)
timeArray=timeArray/float(frecuencia)
print timeArray

#Grafica
plot(timeArray, senal,'k',label=r"$Mi$ $voz$")
ylabel('$Amplitud$', fontsize=18)
xlabel('$Time$ $(s)$', fontsize=18)
plt.title('$SONIDO$'' ''$ORIGINAL$'' ''$GENERADO$', fontsize=20)
legend(loc=0)
savefig("mi_voz.png")
show()

Frecuencia_fundamental=1/frec
print Frecuencia_fundamental


