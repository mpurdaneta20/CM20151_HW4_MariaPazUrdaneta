# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>


from pylab import *

from scipy.io import wavfile


#Se podria usar %load grafica_mi_voz.py para llamar el archivo, pero se genera todo el proceso de nuevo cuando solo se necesita la frecuencia y la señal.

#Se abre el archivo y se obtiene la frecuencia y la señal del sonido generado
frecuencia, senal = wavfile.read('nombre.wav')

#Genera amplitudes de -1,1
senal=senal/2.**15

from scipy.fftpack import fft, fftfreq
import numpy as np

#Transformada de Fourier (TDF) 
fft_senal =fft(senal) / len(senal)
fft_senal=abs(fft_senal)
frec = fftfreq(len(senal), 1) 
plot(abs(frec),fft_senal, 'k',label=r"$TRF$")
xlabel('$Frecuencia$', fontsize=18)
ylabel('$Amplitud$', fontsize=18)
plt.title('$TRANSFORMADA$'' ''$DE$'' ''$FOURIER$', fontsize=20)
legend(loc=0)
savefig("mivoz_fft.png")
show()

MAXIMO=max(fft_senal)
POSICION=MAXIMO
print MAXIMO

plot(abs(frec),fft_senal, 'k')
xlabel('$Frecuencia$', fontsize=18)
ylabel('$Amplitud$', fontsize=18)
plt.title('$TRANSFORMADA$'' ''$DE$'' ''$FOURIER$', fontsize=20)
plot(POSICION,MAXIMO,'ro')
show()
#Basandose en la teoria fisica, se tiene que para las ondas de tipo "SAWTOOTH" el maximo armonico es igual a la maxima amplitud. Dado que n=1 se tiene que Armonico_n=(1/n)*Amplitud_n, luego para 1 Armonico_max=Amplitud_1



