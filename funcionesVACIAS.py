# -*- coding: utf-8 -*-
from configuracion import *
from principal import *
import math
import random

def unaAlAzar(lista):
    #elige una letra al azar
    letra=random.choice(lista)
    return letra

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    puntos=0
    existe=False
    acierto=False
    #recorro la lista de items por posicion
    for i in range(len(items)):
        # encuentro la posicion del item en juego
        if items[i]==item:
            #le paso la posicion a la listaDeTodo y recorro los elementos
            for elemento in listaDeTodo[i]:
                #evalua si existe elemento con esa letra
                if elemento.lower()[0]==letra:
                    existe=True
                    #evalua si la palabra del usuario es igual al elemento
                    if elemento.lower()==palabraUsuario:
                        acierto=True
            # si acerto suma 10 puntos
            if acierto:
                puntos=puntos+10
            # si existe elemento pero el usuario no acerto resta 5 puntos
            if existe and not acierto:
                puntos=puntos-5
    return puntos

def juegaCompu(letraAzar, listaDeTodo):
    salida=[]
    subLista=[]
    for lista in listaDeTodo:
        for elemento in lista:
            #si la primera letra del elemento es igual a la letra al azar agrego el elemento a una sublista
            if elemento.lower()[0]==letraAzar :
                subLista.append(elemento)
        #si la sublista tiene elementos elijo uno al azar y lo agrego a la lista de salida
        if len(subLista)>0:
            elemenAzar=random.choice(subLista)
            salida.append(elemenAzar)
        else:
            #sino agrego un elemento vacio a la lista
            salida.append("------------------")
        #reinicio la sublista
        subLista=[]
    return  salida

def lectura(archivo):
    #realizar lectura del archivo
    lista=archivo.readlines()
    lista=limpiarLista(lista)
    return lista

def limpiarLista(lista):
    nueva_lista=[]
    palabra=""
    #limpiar acentos , dieresis
    for elem in lista:
        for char in elem:
            char=char.replace("á","a")
            char=char.replace("é","e")
            char=char.replace("í","i")
            char=char.replace("ó","o")
            char=char.replace("ú","u")
            char=char.replace("ü","u")
            #limpiar cualquier caracter que no sea una letra o numero
            if (char.lower()>="a" and char.lower()<="z") or char.lower()=="ñ" or char==" " or (char>="0" and char<="9"):
                palabra=palabra+char
        nueva_lista.append(palabra)
        palabra=""
    return nueva_lista

def sumaListas(listavieja, listanueva):
    #sumar ambas listas
    for i in range(5):
        listavieja[i]=int(listavieja[i])+int(listanueva[i])
    return listavieja

def guardarResultados(archivo,resultados):
    #escribe los elementos de la lista en un archivo
    for elem in resultados:
        archivo.write(str(elem)+"\n")
    return archivo

def restablecerEstadistica(archivo):
    #escribe el valor "0" 5 veces en un archivo
    for i in range(5):
        archivo.write("0\n")

def promedioTiempo(lista):
    #dividir el tiempo con la cantidad de intentos para calcular el promedio
    promedio=int(lista[3])/int(lista[4])
    return round(promedio)
