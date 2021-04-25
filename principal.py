#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math, os, random, sys ,codecs
import pygame
from pygame.locals import *
from configuracion import *
from funcionesVACIAS import *
from extras import *



def main():

    # centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    # preparar la ventana
    pygame.display.set_caption("TutiFrutiUNGS")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #agregar musica de fondo
    pygame.mixer.music.load("sonido.mp3")
    pygame.mixer.music.play(10)
    #agregar efecto de sonido
    sonido = pygame.mixer.Sound("acierto.ogg")

    #agregar imagen de fondo
    imagenFondo = pygame.image.load("fruta2.png")
    #ajustar tamaño imagen
    imagenFondo = pygame.transform.scale(imagenFondo,(800,600))

    # Tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    fps = FPS_INICIAL

    #abecedario e items
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    items = ["colores","animales","frutas","verduras","deportes","paises","cap. de paises"]

    #cargar archivos de categorias
    #cadecs lo que permite es establecer con que formato de caracteres se va a leer el archivo, pasandole "utf-8" como argumento a la funcion
    colores = codecs.open("colores.txt","r","utf-8")
    listaColores = lectura(colores)  #lectura del archivo
    colores.close()

    animales = codecs.open("animales.txt","r","utf-8")
    listaAnimales = lectura(animales)
    animales.close()

    frutas = codecs.open("frutas.txt","r","utf-8")
    listaFrutas = lectura(frutas)
    frutas.close()

    verduras = codecs.open("verduras.txt","r","utf-8")
    listaVerduras = lectura(verduras)
    verduras.close()

    deportes = codecs.open("deportes.txt","r","utf-8")
    listaDeportes = lectura(deportes)
    deportes.close()

    paises = codecs.open("paises.txt","r","utf-8")
    listaPaises = lectura(paises)
    paises.close()

    capitales = codecs.open("capitalesDePaises.txt","r","utf-8")
    listaCapitales = lectura(capitales)
    capitales.close()

    #carga de archivo de estadisticas
    estadistica = open("estadistica.txt","r")
    listaEstadisticaInicial = lectura(estadistica)
    estadistica.close()

    #iniciar variables y listas
    puntos = 0
    aciertos = 0
    errores = 0
    listaDeTodo = [listaColores,listaAnimales,listaFrutas,listaVerduras,listaDeportes,listaPaises,listaCapitales]
    letraAzar = unaAlAzar(abc)
    palabraUsuario = ""
    eleccionUsuario = []
    eleccionCompu = []
    listaResultados = []
    listaValidacion = []

    i = 0
    while i<len(items):
        # 1 frame cada 1/fps segundos
        gameClock.tick()
        totaltime += gameClock.get_time()/1000
        fps = 3

        # buscar la tecla presionada del modulo de eventos de pygame
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
            if e.type == KEYDOWN:
                letra = dameLetraApretada(e.key)
                palabraUsuario += letra
                if e.key == K_BACKSPACE:
                    palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                if e.key == K_RETURN:
                    #ejecutar efecto de sonido
                    sonido.play()
                    eleccionUsuario.append(palabraUsuario)
                    sumar = 0
                    #chequea si es correcta suma 10 puntos sino resta 5 puntos
                    sumar = esCorrecta(palabraUsuario, letraAzar, items[i], items, listaDeTodo)
                    puntos = puntos+sumar
                    #chequea la cantidad de aciertos
                    if sumar == 10:
                        aciertos = aciertos+1
                        listaValidacion.append(1)
                    #chequea la cantidad de errores
                    elif sumar == -5:
                        errores = errores+1
                        listaValidacion.append(-1)
                    else:
                        listaValidacion.append(0)
                    palabraUsuario = ""
                    i = i + 1
        #segundos = pygame.time.get_ticks() / 1000
        # limpiar pantalla anterior
        screen.blit(imagenFondo,(0,0))
        if i<len(items):
            dibujar(screen, letraAzar, items[i], palabraUsuario, puntos, totaltime)
        else:
            intento=1
            eleccionCompu = juegaCompu(letraAzar, listaDeTodo)
            #agregar los resultados (puntos, aciertos, errores, tiempo, intentos) a una lista
            listaResultados.append(puntos)
            listaResultados.append(aciertos)
            listaResultados.append(errores)
            listaResultados.append(round(totaltime))
            listaResultados.append(intento)
            #sumar los resultados con los del intento anterior
            resultados = sumaListas(listaEstadisticaInicial,listaResultados)
            #guardar resultados en un archivo
            archivo = open("estadistica.txt","w")
            resultados = guardarResultados(archivo,resultados)
            archivo.close()
            dibujarSalida(screen, letraAzar, items, eleccionUsuario, eleccionCompu, puntos, totaltime,listaValidacion)
            pygame.display.flip()

            while True:
                for e in pygame.event.get():
                    if e.type == KEYDOWN:
                        if e.key == K_s:
                            #reinicia el juego
                            main()
                            return
                        if e.key == K_ESCAPE:
                            screen.blit(imagenFondo,(0,0))
                            #mostrar estadisticas del juego
                            archivo = open("estadistica.txt","r")
                            listaEstadisticaFinal=lectura(archivo)
                            promedio = promedioTiempo(listaEstadisticaFinal)
                            archivo.close()
                            dibujarResultado(screen,listaEstadisticaFinal,promedio)
                            pygame.display.flip()
                    if e.type == QUIT:
                        #resetear el archivo de estadisticas
                        archivo = open("estadistica.txt","w")
                        restablecerEstadistica(archivo)
                        archivo.close()
                        pygame.quit()
                        return

        pygame.display.flip()

if __name__ == '__main__':
    main()