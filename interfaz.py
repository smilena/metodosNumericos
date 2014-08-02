#modulos y librerias necesarias
import math
import Pmw
import csv
from scipy import linspace,polyval
from tkFileDialog import askopenfilename
from Tkinter import *
from estadistica import Estadistica
from polinomio import Polinomio
from regresion import Regresion
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg


#Funciones Estadistica***************************************************************************

datosEstadistica = []
#objeto operaciones, con el cual sera posible acceder a todos las operaciones de la clase Estadistica
operaciones=Estadistica(datosEstadistica)
#funcion que permite leer los datos
def elegirArchivoEstadistica():
    try:	
        nombreArchivo=askopenfilename()
        lectura = csv.reader(open(nombreArchivo, 'rb'))
        for i in lectura:
            datosEstadistica.append(int("".join(i)))
        operaciones.setDatos(datosEstadistica)
    except:
	print "ha ocurrido un error"

#funcion encargada de enviar los valores obtenidos a los objetos Label indicados por medio
#de la funcion "set"
def operaciones_estadistica():
    moda.set(operaciones.moda())
    media.set(operaciones.media())
    mediana.set(operaciones.mediana())
    desviacionMedia.set(operaciones.desviacion_media(operaciones.media()))
    desviacionEstandar.set(operaciones.desviacion_estandar(operaciones.media()))


def dibujar_histograma():    
    sub_figura = f.add_subplot(111)
    frecuencias_absolutas=[]
    frecuencias_absolutas=list(np.bincount(operaciones.getDatos()))
    frecuencias_absolutas.sort()
    tamFrecuenciasAbsolutas=len(frecuencias_absolutas)
    #Se genera el histograma
    sub_figura.hist(operaciones.getDatos(), tamFrecuenciasAbsolutas, facecolor='green',alpha=0.75)
    #nombre del eje X
    sub_figura.set_xlabel('Datos')
    #nombre del eje y
    sub_figura.set_ylabel('Frecuencia Absoluta')
    #titulo
    sub_figura.set_title('HISTOGRAMA')
    #tamano de los ejes
    sub_figura.axis([0, tamFrecuenciasAbsolutas, 0, frecuencias_absolutas[tamFrecuenciasAbsolutas-1]+1])
    #dibujar cuadricula y asi tener una guia
    sub_figura.grid(True)
    global canvasHistograma 
    #muestra el histograma en un canvas que se ha anadido anteriormente
    canvasHistograma.show()

#ventana principal
root=Pmw.initialise()
#conjunto de paginas que se agrega a la ventana principal
notebook = Pmw.NoteBook(root)
notebook.pack(fill = 'both', expand = 1, padx = 10, pady = 10)

#anadiendo paginas o pestanas
page_0 = notebook.add('Inicio')
page_1 = notebook.add('Estadistica')
page_2 = notebook.add('R. Lineal')
page_3 = notebook.add('P. Aproximador')
page_4 = notebook.add('Ayuda')
#por defecto la pestana o pagina inicio estara seleccionada
notebook.tab('Inicio').focus_set()

#Interfaz estadistica ***************************************************************************

#Objetos de interfaz grafica, etiquetas, botones, canvas (areas de dibujo)
labelEstadistica = Label(page_1, text = 'ESTADISTICA')
labelEstadistica.grid(row = 0, column = 2,sticky=E)
instruccionEstadistica = Label(page_1, text = 'Elija archivo CSV, para obtener los datos: ')
instruccionEstadistica.grid(row = 1, column = 0,columnspan=3,sticky=W)
botonExaminarEstadistica = Button(page_1, text = 'Examinar', command = elegirArchivoEstadistica)
botonExaminarEstadistica.grid(row = 1,column = 3,sticky=W)
botonCalcularEstadistica = Button(page_1, text = 'Calcular', command = operaciones_estadistica)
botonCalcularEstadistica.grid(row = 1, column = 4,sticky=W)

labelModa = Label(page_1, text = 'Moda:')
labelModa.grid(row = 2, column = 0,sticky=W)
moda = StringVar()
resultadoModa=Label(page_1,textvariable=moda)
resultadoModa.grid(row=2,column=1,sticky=W)
labelMedia=Label(page_1,text="Media:")
labelMedia.grid(row=2,column=2,sticky=W)
media=StringVar()
resultadoMedia=Label(page_1,textvariable=media)
resultadoMedia.grid(row=2,column=3,sticky=W)
labelMediana=Label(page_1,text="Mediana:")
labelMediana.grid(row=2,column=4,sticky=W)
mediana=StringVar()
resultadoMediana=Label(page_1,textvariable=mediana)
resultadoMediana.grid(row=2,column=5,sticky=W)
labelDesviacionMedia=Label(page_1,text="D. Media")
labelDesviacionMedia.grid(row=3,column=0,sticky=W)
desviacionMedia=StringVar()
resultadoDesviacionMedia=Label(page_1,textvariable=desviacionMedia)
resultadoDesviacionMedia.grid(row=3,column=1,sticky=W)
labelDesviacionEstandar=Label(page_1,text="D. Estandar")
labelDesviacionEstandar.grid(row=3,column=2,sticky=W)
desviacionEstandar=StringVar()
resultadoDesviacionEstandar=Label(page_1,textvariable=desviacionEstandar)
resultadoDesviacionEstandar.grid(row=3,column=3,sticky=W)
botonHistograma=Button(page_1,text="Generar Histograma",command=dibujar_histograma)
botonHistograma.grid(row=4,column=2)

#Figura que se agregara al frame
f = Figure(figsize=(5,4),dpi=100)
canvasHistograma= FigureCanvasTkAgg(f, master=page_1)

#Ubicacion del area de dibujo
canvasHistograma.get_tk_widget().grid(row=5,columnspan=6)

#Funciones R. Lineal ***************************************************************************

datosXRegresion=[]
datosYRegresion=[]
#objeto regresion, con el cual sera posible acceder a todos las operaciones de la clase Regresion
regresion=Regresion(datosXRegresion,datosYRegresion)

#funcion que permite leer los datos
def elegirArchivoRegresion():
    try:	
        nombreArchivo=askopenfilename()
        lectura = csv.reader(open(nombreArchivo, 'rb'))
        for i in lectura:
            datosXRegresion.append(int(i[0]))
	    datosYRegresion.append(int(i[1]))
        regresion.setX(datosXRegresion)
	regresion.setY(datosYRegresion)
    except:
	print "ha ocurrido un error"

#funcion encargada de enviar los valores obtenidos a los objetos Label indicados por medio
#de la funcion "set"
def operaciones_regresion():
    coeficienteCorrelacion.set(regresion.coeficiente_correlacion())
    a=regresion.getA()
    b=regresion.getB(a)
    signoA=""
    signoB=" + "
    if(a<0):
	a*=-1
	signoA="- "
    if(b<0):
	b*=-1
	signoB=" - "
    ecuacion.set("Y = "+signoA+str(a)+"X"+signoB+str(b))


def dibujar_regresion():
    sub_figura = figuraRegresion.add_subplot(111)
    n=len(regresion.getX())
    t=linspace(0,max(regresion.getX()),n)
    a=regresion.getA()
    b=regresion.getB(a)
    x=polyval([a,b],t)
    #dibuja la regresion en el espacio dado
    sub_figura.plot(t,x,'g.--')
    sub_figura.plot(regresion.getX(),regresion.getY(),'k.')
    sub_figura.set_xlabel('X (variable independiente)')
    sub_figura.set_ylabel('Y (variable dependiente)')
    sub_figura.set_title("REGRESION LINEAL")
    sub_figura.grid(True)
    global canvasRegresion 
    canvasRegresion.show()

#Interfaz R. Lineal ***************************************************************************

#Objetos de interfaz grafica, etiquetas, botones, canvas (areas de dibujo)
labelRegresion=Label(page_2,text="REGRESION LINEAL")
labelRegresion.grid(row=0,column=1,columnspan=2)
labelInstruccionesRegresion=Label(page_2,text="Elija archivo CSV, para obtener los datos: ")
labelInstruccionesRegresion.grid(row=1,column=0,columnspan=2,sticky=W)
botonExaminarRegresion=Button(page_2,text="Examinar",command=elegirArchivoRegresion)
botonExaminarRegresion.grid(row=1,column=2,sticky=W)
botonCalcularRegresion=Button(page_2,text="Calcular",command=operaciones_regresion)
botonCalcularRegresion.grid(row=1,column=3,sticky=W)

labelCorrelacion=Label(page_2,text="Coeficiente de correlacion:")
labelCorrelacion.grid(row=2,column=0,columnspan=2,sticky=W)
coeficienteCorrelacion=StringVar()
resultadoCorrelacion=Label(page_2,textvariable=coeficienteCorrelacion)
resultadoCorrelacion.grid(row=2,column=2,sticky=W)
labelDescripcionEcuacion=Label(page_2,text="La ecuacion de la recta que mejor ajusta los datos es: ")
labelDescripcionEcuacion.grid(row=3,column=0,columnspan=3,sticky=W)
ecuacion=StringVar()
labelEcuacionRegresion=Label(page_2,textvariable=ecuacion)
labelEcuacionRegresion.grid(row=3,column=3,sticky=W)
botonDibujarRegresion=Button(page_2,text="Dibujar Regresion Lineal",command=dibujar_regresion)
botonDibujarRegresion.grid(row=4,column=1,columnspan=2)


#Figura que se agregara al frame
figuraRegresion = Figure(figsize=(5,4),dpi=100)
canvasRegresion= FigureCanvasTkAgg(figuraRegresion, master=page_2)


#Ubicacion del area de dibujo
canvasRegresion.get_tk_widget().grid(row=5,columnspan=5)

#Funciones P. Aproximador ***************************************************************************

datosXPolinomio=[]
datosYPolinomio=[]
#objeto polinomio el cual permite acceder a las funciones de la clase Polinomio
polinomio=Polinomio(datosXPolinomio,datosYPolinomio)

#funcion que permite leer los datos
def elegirArchivoPolinomio():   
    try:	
        nombreArchivo=askopenfilename()
        lectura = csv.reader(open(nombreArchivo, 'rb'))
        for i in lectura:
            datosXPolinomio.append(int(i[0]))
            datosYPolinomio.append(int(i[1]))
        polinomio.setX(datosXPolinomio)
        polinomio.setY(datosYPolinomio)
    except:
        print "ha ocurrido un error"

#funcion que permite calcular y mostrar el sistema de ecuaciones, agregandolo a un objeto label
def calcular_sistema_ecuaciones():
    coeficientes = polinomio.getCoeficientes(int(entryGrado.get()))
    resultados = polinomio.getResultados(int(entryGrado.get()))
    string=""
    j=0
    for i in range(len(coeficientes)):
	for j in range(len(coeficientes)):
	    string+=str(coeficientes[i][j])+'\t'
        string+='=\t'+str(resultados[i])+'\n'
    sistemaEcuaciones.set(string)
    polinomio.getCoeficientes(int(entryGrado.get()))  

##funcion que permite calcular y mostrar la solucion del sistema de ecuaciones, 
#agregandolo a un objeto label
def calcular_solucionn_seidel():
    grado=int(entryGrado.get())
    coeficientes = polinomio.getCoeficientes(grado)
    resultados = polinomio.getResultados(grado)
    valores_nuevos=[]
    valores=[]
    for i in range(grado+1):
	valores.append(0)
	valores_nuevos.append(0)
    error=1
    while(error>0.001):
	for i in range(len(valores)):
	    suma=0.0
	    for j in range(len(coeficientes)):
		if(i!=j):
		    suma-=valores_nuevos[j]*coeficientes[i][j]
	    valores_nuevos[i]=round((suma+resultados[i])/coeficientes[i][i],4)
        for i in range(len(valores)):
	    if(valores_nuevos[i] != 0):
	        error_actual=abs((valores_nuevos[i]-valores[i])/valores_nuevos[i])
	    if(error_actual<error):
	        error=error_actual 
	valores=valores_nuevos
	valores_nuevos
    string='\n'
    for i in range(len(valores)):
        string+=str(valores[i])+'\t'
    solucionSeidel.set(string)

#Interfaz P. Aproximador ***************************************************************************

#Objetos de interfaz grafica, etiquetas, botones, canvas (areas de dibujo)
labelPolinomio=Label(page_3,text='POLINOMIO APROXIMADOR')
labelPolinomio.grid(row=0,column=1,columnspan=2)
labelInstruccionesPolinomio=Label(page_3,text='\nElija archivo CSV, para obtener los datos: ')
labelInstruccionesPolinomio.grid(row=1,column=0,columnspan=2,sticky=W)
botonExaminarPolinomio=Button(page_3,text='Examinar',command=elegirArchivoPolinomio)
botonExaminarPolinomio.grid(row=1,column=2,sticky=W)
labelGrado=Label(page_3,text='\nIngrese grado del polinomio')
labelGrado.grid(row=2,column=0,sticky=W)
entryGrado=Entry(page_3,width=3)
entryGrado.insert(0,'0')
entryGrado.grid(row=2,column=1,sticky=W)
botonCalcularSistema=Button(page_3,text='Calcular S.E.',command=calcular_sistema_ecuaciones)
botonCalcularSistema.grid(row=2,column=2)
botonCalcularSeidel=Button(page_3,text='Solucion Seidel.',command=calcular_solucionn_seidel)
botonCalcularSeidel.grid(row=2,column=3)
labelTituloSistema=Label(page_3,text='\nSISTEMA DE ECUACIONES')
labelTituloSistema.grid(row=3,column=0,sticky=W)
sistemaEcuaciones=StringVar()
labelSistemaEcuaciones=Label(page_3,textvariable=sistemaEcuaciones)
labelSistemaEcuaciones.grid(row=4,column=0,sticky=W,columnspan=5)
labelTituloSeidel=Label(page_3,text='\nRESULTADO SEIDEL')
labelTituloSeidel.grid(row=5,column=0,sticky=W)
solucionSeidel=StringVar()
labelSolucionSeidel=Label(page_3,textvariable=solucionSeidel)
labelSolucionSeidel.grid(row=6,column=0,sticky=W,columnspan=5)

#Interfaz Inicio ***************************************************************************

#Mensaje donde se especifica la licencia del software, su titulo, lenguaje, dependencias y
#contacto del desarrollador
mensajeInicio = """
    <Numerical Stuff: this software bring to you the opportunity of test
     several numerical methods.>
    <language: Python2.6>
    <dependences: Scipy,Pylab,matplotlib,math,Pmw,tkFileDialog,Tkinter>

    Copyright (C) <2012>  <Sandra Milena Guevara> <smilena89@gmail.com>


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    This software is part of a undergraduate research work at UD 
    <www.udistrital.edu.co>, it is licenced under the GNU/GPL v3.
    You can redistribute,modify and share this code always without forget 
    reference the original author cited in the beginning of this document.
    

    If not, see <http://www.gnu.org/licenses/>.
    @milenaguevara

"""
labelMensajeInicio=Label(page_0,text=mensajeInicio,justify=LEFT)
labelMensajeInicio.grid(row=0,column=0,columnspan=3)

#Interfaz Ayuda ***************************************************************************

#Mensaje que indica la ayuda necesaria para el manejo del software
mensajeAyuda="""
                                                      AYUDA
ESTADISTICA

1. Suministe sus datos a traves de un archivo CSV, para el cual cada renglon 
   representara un dato.
2. Oprima el boton Calcular para obtener los valores de las medidas de 
   dispersion Moda, Media, Mediana, D. Media y D. Esrandar.
3. Oprima el boton Generar Histograma para visualizar el histograma que 
   representa los datos.

REGRESION LINEAL

1. Suministe sus datos a traves de un archivo CSV, para el cual cada renglon 
   representara un punto en el plano de la siguiente forma: x,y.
2. Oprima el boton Calcular para obtener el valor del Coeficiente de Correlacion 
   y la ecuacion de la recta.
3. Oprima el boton Regresion Lineal para visualizar el grafico de la regresion 
   lineal que representa los datos.

POLINOMIO APROXIMADOR

1. Suministe sus datos a traves de un archivo CSV, para el cual cada renglon 
   representara un punto en el plano de la siguiente forma: x,y
2. Ingrese el grado del polinomio.
3. Oprima el boton Calcular S.E. para obtener el sistema de ecuaciones.
4. Oprima el boton Solucion Seidel. para obtener la solucion del sistema de 
   ecuaciones por medio del metodo Seidel. 
    
"""

labelMensajeAyuda=Label(page_4,text=mensajeAyuda,justify=LEFT)
labelMensajeAyuda.grid(row=0,column=0,columnspan=3)

notebook.setnaturalsize()
#Se desactiva la propiedad resizable de la ventana principal 
root.resizable(FALSE,FALSE)
#Titulo del sofware
root.title('Numerical Stuff')
root.mainloop()
