#modulos
from numpy import *
import math
#clase Regresion
class Regresion():
    #listas de la coleccion de puntos 
    x=[]
    y=[]
    #constructor
    def __init__(self,x,y):
	self.x=x
	self.y=y

    #metodo que permite actualizar la propiedad x
    def setX(self,x):
	self.x=x
  
    #metodo que permite obtener el valor de la propiedad x
    def getX(self):
	return self.x

    #metodo que permite actualizar la propiedad y
    def setY(self,y):
	self.y=y

    #metodo que permite obtener el valor de la propiedad y
    def getY(self):
	return self.y

    #metodos que permite hallar el coeficiente de correlacion 
    def coeficiente_correlacion(self):
	mediaX=mean(self.x)
	mediaY=mean(self.y)
	n=len(self.x)
        suma=sumaCuadradosX=sumaCuadradosY=0.0
	for i in range(len(self.x)):
	    suma+=((self.x[i]-mediaX)*(self.y[i]-mediaY))
            sumaCuadradosX+=(self.x[i]-mediaX)**2
	    sumaCuadradosY+=(self.y[i]-mediaY)**2
        desviacionEstandarX=math.sqrt(sumaCuadradosX/n)
	desviacionEstandarY=math.sqrt(sumaCuadradosY/n)
        return round(suma/(n*desviacionEstandarX*desviacionEstandarY),2)

    #metodo que permite hallar coeficiente A de la ecuacion
    def getA(self):
	sumXY=sumX=sumY=sumXcuadrado=0.0
	n=len(self.x)
	for i in range(len(self.x)):
	    sumXY+=(self.x[i]*self.y[i])
	    sumX+=self.x[i]
	    sumY+=self.y[i]
	    sumXcuadrado+=self.x[i]**2
	numerador=(n*sumXY)+(sumX*sumY)
	denominador=(n*sumXcuadrado)-(sumX**2)
	return round(numerador/denominador,3)

    #metodo que permite hallar coeficiente B de la ecuacion
    def getB(self,a):
	sumY=sumX=0.0
	n=len(self.x)
	for i in range(len(self.x)):
	    sumX+=self.x[i]
	    sumY+=self.y[i]
	numerador=sumY-a*sumX
	denominador=n
	return round(numerador/denominador,3)










