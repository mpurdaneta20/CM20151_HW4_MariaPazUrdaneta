# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#PUNTO 1B
from pylab import *


import csv
import matplotlib.pyplot as plt
import pandas
from pandas import *

df_bog=pandas.read_csv('Bogota.csv', sep=' ')
df_bquilla=pandas.read_csv('Barranquilla.csv', sep=' ')
df_bucara=pandas.read_csv('Bucaramanga.csv', sep=' ')
df_cali=pandas.read_csv('Cali.csv', sep=' ')
df_ipiales=pandas.read_csv('Ipiales.csv', sep=' ')

F_bog=df_bog['yr']
F_bquilla=df_bquilla['yr']
F_bucara=df_bucara['yr']
F_cali=df_cali['yr']
F_ipiales=df_ipiales['yr']

Temp_bog=df_bog['Temperatura']
Temp_bquilla=df_bquilla['Temperatura']
Temp_bucara=df_bucara['Temperatura']
Temp_cali=df_cali['Temperatura']
Temp_ipiales=df_ipiales['Temperatura']

L=range(len(Temp_bog))


#ORIGINAL
plot(F_bog,Temp_bog,label=r"$Bogota$")
plot(F_bquilla,Temp_bquilla,label=r"$Baranquilla$")
plot(F_bucara,Temp_bucara,label=r"$Bucaramanga$")
plot(F_cali,Temp_cali,label=r"$Cali$")
plot(F_ipiales,Temp_ipiales,label=r"$Ipiales$")
legend(loc=0, fontsize=7)
title("Temperatura ciudades de Colombia")
ylabel('Temperatura')
xlabel('Yr')
show()

#INTERPOLACION LINEAL
LIN_bog=Series(Temp_bog).interpolate()
LIN_bquilla=Series(Temp_bquilla).interpolate()
LIN_bucara=Series(Temp_bucara).interpolate()
LIN_cali=Series(Temp_cali).interpolate()
LIN_ipiales=Series(Temp_ipiales).interpolate()

plot(F_bog,LIN_bog,label=r"$Bogota$")
plot(F_bquilla,LIN_bquilla,label=r"$Baranquilla$")
plot(F_bucara,LIN_bucara,label=r"$Bucaramanga$")
plot(F_cali,LIN_cali,label=r"$Cali$")
plot(F_ipiales,LIN_ipiales,label=r"$Ipiales$")
legend(loc=0, fontsize=7)
title("Temperatura ciudades de Colombia - Interp. Lineal")
ylabel('Temperatura')
xlabel('Yr')
show()

#INTERPOLACION POLINOMICA (Grado 2)
POL_bog=Series.interpolate(Temp_bog,method='quadratic')
POL_bquilla=Series.interpolate(Temp_bquilla, method='quadratic')
POL_bucara=Series.interpolate(Temp_bucara,method='quadratic')
POL_ipiales=Series.interpolate(Temp_ipiales, method='quadratic')
POL_cali=Series.interpolate(Temp_cali,method='quadratic')

plot(F_bog,POL_bog,label=r"$Bogota$")
plot(F_bquilla,POL_bquilla,label=r"$Baranquilla$")
plot(F_bucara,POL_bucara,label=r"$Bucaramanga$")
plot(F_cali,POL_cali,label=r"$Cali$")
plot(F_ipiales,POL_ipiales,label=r"$Ipiales$")
legend(loc=0, fontsize=7)
title("Temperatura ciudades de Colombia - Interp. Cuadratica")
ylabel('Temperatura')
xlabel('Yr')
show()

#Interpolacion por splines
SP_bog=Temp_bog.interpolate(method='spline', order=3)
SP_bquilla=Temp_bquilla.interpolate(method='spline', order=3)
SP_bucara=Temp_bucara.interpolate(method='spline', order=3)
SP_ipiales=Temp_ipiales.interpolate(method='spline', order=3)
SP_cali=Temp_cali.interpolate(method='spline', order=3)

plot(F_bog,SP_bog,label=r"$Bogota$")
plot(F_bquilla,SP_bquilla,label=r"$Baranquilla$")
plot(F_bucara,SP_bucara,label=r"$Bucaramanga$")
plot(F_cali,SP_cali,label=r"$Cali$")
plot(F_ipiales,SP_ipiales,label=r"$Ipiales$")
legend(loc=0, fontsize=7)
title("Temperatura ciudades de Colombia - Interp. Spline")
ylabel('Temperatura')
xlabel('Yr')
show()

#Conclusion: Mejor predictor 
#Aunque en realidad el primer grafico de la serie de tiempo pertenece a una distribucion discreta se genera con lineas (continua con saltos) para que sea mas simple la comparacion entre el original y la extrapolacion de datos que rellenaria la serie con datos estimados a partir de los datos originales.

#A simple vista el que mejor parece ajustarse a los datos  es el metodo de spline, seguido por el lineal y finalmente el cuadratico. Con respecto al metodo cuadratico se observa que arroja datos muy incoerentes que se salen del rango de Temperaturas normales para Colombia

plot(F_bog,LIN_bog,label=r"$Bogota_LIN$")
plot(F_bog,POL_bog,label=r"$Bogota_POL$")
plot(F_bog,SP_bog,label=r"$Bogota_SP$")

legend(loc=0, fontsize=7)
title("Temperatura ciudades de Colombia - Interp.")
ylabel('Temperatura')
xlabel('Yr')
show()

#Se observa que la interpolacion por spline y la lineal se encuentran en rangos normales y tienen una secuencia consistente entre los datos predichos y los datos dados.

#Los archivos .csv para cada una de las ciudades son generados a partir de el script .R hay que tener cuidado porque en ocasiones no se guardan en la carpeta en la cual se esta trabajando
#!("rm Bogota.csv")
#!("rm Barranquilla.csv")
#!("rm Bucaramanga.csv")
#!("rm Cali.csv")
#!("rm Ipiales.csv")

