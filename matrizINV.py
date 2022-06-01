import numpy as np

# -*- coding: utf-8 -*-
# Created on May 27 10:41:19 2022
# @author: Jesus  D. Redondo 
# Reto propuesto por Dr Aldo Combariza
'''
    Enunciado:
        Dada una matriz de dimensiones MxM calcular su inversa
        utilizando solamente itereadores como lo son los bucles
        for y While.
    
    Variables:
        A lo largo del codigo nos encontraremos variables 
        fundamentales para el correcto funcionamiento aqui explicare
        alguna de ellas.
        
        array:
            Esta variable contendra la matriz a la cual queremos hallar
            su inversa, cabe resaltar que esta matriz se genera aleatoriamente
            para optimizar tiempo de escritura, si el usuario lo desea puede 
            introducir su propia matriz siempre y cuando sea MxM
        
        identidad:
            Esta variable contendra la matriz identidad la cual se genera 
            dependiendo el tamaño de la matriz para luego emplear el metodo
            de Gauss-Jordan. 
            Nota: A continuacion se puede observar que esta variable se crea 
            con bucles NADA DE LIBRERIAS
        
        pivote:
            corresponde al pivote de la fila y lo utilizamos para hacer 
            calculos pertinentes como cambio de fila si este es cero etc
         
        numero:
            hece referencia a la razon entre el pivote y la posicion 
            en que se encuentra el itereador, es importante reducir la matriz.
        
    Funciones:
        Encontraremos 3 funciones las cuales son:
        
        cambio_de_fila:
            Como su nombre lo indica la utilizaremos para cambiar las filas cuando
            se nos presente la situacion que el pivote es igual a cero.
        
        eliminacion:
            Esta funcion es importante a la hora de reducir la matriz
            puesto que se aumentara la fila a razon del pivote dado y despues 
            se hara la resta o suma.
        
        inversa:
            En este funcion tendra dos puntos importantes:
                1._eliminacion hacia delante:
                    Esta eliminacion consiste en que cada numero que
                    se encuentre por debajo del pivote hacerlo cero 
                    y asi iremos formando la matriz identidad

                2._eliminacion hacia atras:
                    Comenzaremos iterando desde la ultima fila hasta la 
                    primera y cada numero por encima del pivote hacerlo cero 
                    y como ultimo paso dividir toda la fila por el valor del
                    pivote para que asi nos queda la matriz identidad y al lado 
                    la matriz INVERSA
    
    Para hallar la inversa se ira iterando sobre la matriz dada y se iran replicando esos
    mismo calculos en la matriz identidad - los calculo puede comprobarlos en https://www.wolframalpha.com/
    y asi corroborar que todo funciona correctamente
'''


array = np.random.randint(1,12, size=(3,3))
array = np.array(array)
array = array.astype(float)
matrizI = []
#Creamos una matriz de Ceros
for i in range(array.shape[0]):
    matrizI.append([0]*array.shape[0])
count=0

#Iteramos cada fila para hacer la matriz identiad (I)
for j in matrizI:
    j[count] =  1 
    matrizI[count] = j
    count+=1

def cambio_de_fila(matriz,i):
    for k in range(i+1,len(matriz)):
        if matriz[k][i] != 0:
            temp = matriz[k].copy()
            matriz[k] = matriz[i].copy()
            matriz[i] = temp.copy()
            return matriz

def eliminacion(matriz_convertir,matriz_pivote,numero):
    lista= []
    nueva_lista=[]
    for i in matriz_convertir:
        valor = numero*i
        lista.append(valor)
    for j in range(len(matriz_pivote)):
        resta = round(lista[j]-matriz_pivote[j],3)
        nueva_lista.append(resta)
    return nueva_lista

def inversa(matriz,identidad):
   
    print("---"*30)
    print("la matriz es:\n",matriz)
    print("---"*30)
    #1._ Eliminacion hacia delante
    for i in range(len(matriz)):
        if matriz[i][i]==0:
            matriz=cambio_de_fila(matriz,i)
            identidad=cambio_de_fila(identidad,i)
        pivote = matriz[i][i]
        for j in range(len(matriz)):
            if i != j  and matriz[j][i] != 0:
                numero = pivote/matriz[j][i] #Se hace el calculo para los pivotes de abajo
                fila_identidad=eliminacion(identidad[j],identidad[i],numero)
                fila_reducida=eliminacion(matriz[j],matriz[i],numero)
                identidad[j]=fila_identidad
                matriz[j] = fila_reducida
    #eliminacion hacia atras
    for i in range(len(matriz)-1, -1, -1):
        pivote = matriz[i][i]
        anterior = i-1 
        for k in range(anterior,-1,-1):
            if  i != k and matriz[k][i] != 0:
                numero = pivote/matriz[k][i]
                fila_identidad_escalonada=eliminacion(identidad[i],identidad[j],numero)
                fila_escalonada= eliminacion(matriz[i],matriz[k],numero)
                identidad[k]= fila_identidad_escalonada
                matriz[k]=fila_escalonada
        #matriz[k][:] = matriz[k][:] - matriz[i][:]*numero
        identidad[i][:] = identidad[i][:]/matriz[i][i]
        matriz[i][:] = matriz[i][:]/matriz[i][i]
    print("la inversa es:\n", identidad)
identidad = matrizI
identidad=np.array(identidad)
identidad = identidad.astype(float)
inversa(array,identidad)
