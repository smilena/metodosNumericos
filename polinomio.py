#clase Polinomio
class Polinomio():
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

    #metodo que permite actualizar el grado del polinomio
    def setGrado(self,grado):
	self.grado=grado

    #metodo que permite obtener el grado del polinomio
    def getGrado(self):
	return self.grado

    #metodo que calcula el sistema de ecuaciones y retorna una matriz de coeficientes
    def getCoeficientes(self,grado):
	matriz=[]
	for i in range(grado+1):
	    fila=[]
	    for j in range(i,i+grado+1):
		suma=0		
		for k in range(len(self.x)):
		    suma+=self.x[k]**j
		fila.append(suma) 
	    matriz.append(fila)
	return matriz

    #metodos que calcula las variables independientes de cada ecuacion y retorna una lista con cada uno
    def getResultados(self,grado):
	grado+=1
 	resultados=[]
	for i in range(grado):
	    resultado=0
	    for j in range(len(self.y)):
		resultado+=self.y[j]*(self.x[j]**i)
	    resultados.append(resultado)
        return resultados






