#modulos
from numpy import *
#clase Estadistica
class Estadistica():
    #definicion de la lista de datos
    datos=[]
    #constructor de la clase
    def __init__(self,datos):
	self.datos=datos

    #metodo que permite actualizar la propiedad datos
    def setDatos(self,datos):
	self.datos=datos

    #metodo que permite obtener el valor de datos
    def getDatos(self):
	return self.datos

    #metodo que calcula la moda
    def moda(self):
        return list(bincount(self.datos)).index(max(bincount(self.datos)))

    #metodo que calcula la mediana
    def mediana(self):
	tam=len(self.datos)
	if(tam%2 != 0):
	    return tam/2
	else:
	    return round(((self.datos[tam/2])+(self.datos[tam/2+1]))/2.0,5)

    #metodo que calcula la media aritmetica
    def media(self):
	suma=0.0
	tam=len(self.datos)
	for i in range(tam):
	    suma+=self.datos[i]
        return round(suma/tam,5)

    #metodo que calcula la desviacion estandar
    def desviacion_estandar(self,media_aritmetica):
	suma=0.0
	tam=len(self.datos)
	for i in range(tam):
	    suma+=((self.datos[i]-media_aritmetica)**2)
	return round((suma/tam)**(1.0/2.0),5)

    #metodo que calcula la desviacion media
    def desviacion_media(self,media_aritmetica):
	suma=0.0
	tam=len(self.datos)
	for i in range(tam):
	    suma+=abs(self.datos[i]-media_aritmetica)
	return round(suma/tam,5)










        
