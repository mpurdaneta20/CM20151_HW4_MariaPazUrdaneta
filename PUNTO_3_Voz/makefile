#BASE MAKEFILE
#all: p1 p2 p3

#p1: Foo.o main1.o
   #g++ -Wall Foo.o main1.o -o p1

#p2: Bar.o main2.o
   #g++ -Wall Bar.o main2.o -o p2

#p3: Baz.o main3.o
   #g++ -Wall Baz.o main3.o -o p3

#MAKEFILE REAL
all: mivoz_fft.png mi_voz.png nombre.wav grabar_mi_nombre.x

grabar_mi_nombre.x: grabar_mi_nombre.c
	cc grabar_mi_nombre.c -o grabar_mi_nombre.x

nombre.wav:grabar_mi_nombre.x	
	./grabar_mi_nombre.x

mi_voz.png: nombre.wav
	python grafica_mi_voz.py

mivoz_fft.png: fft_de_mi_voz.py
	python fft_de_mi_voz.py

clean:
        rm *.png *.wav *.x

