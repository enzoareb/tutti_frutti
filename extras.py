# -*- coding: utf-8 -*-
import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_1:
        return ("enter")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    elif key == 59:
        return("ñ")
    else:
        return("")

def dibujar(screen, letra, item, palabraUsuario, puntos, segundos):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    #Linea Horizontal
    pygame.draw.line(screen, COLOR_BLANCO, (0, ALTO - 70), (ANCHO, ALTO - 70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_BLANCO), (190, 570))

    #muestra puntos, tiempo, el item y la letra
    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_BLANCO)
    ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_BLANCO )
    ren3 = defaultFontMUYGRANDE.render(item, 1, COLOR_BLANCO)
    ren4 = defaultFontMUYGRANDE.render(letra if letra=="ñ" else letra.upper(), 1, COLOR_ROJO)

    screen.blit(ren1, (ANCHO - 120, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (ANCHO//2-((len(item)//2)*TAMANO_LETRA_GRANDE), ALTO//2))
    screen.blit(ren4, (ANCHO//2-TAMANO_LETRA_GRANDE, 110))

def dibujarSalida(screen, letra, items, eleccionUsuario, eleccioncompu, puntos, segundos,validacion):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA)
    defaultFont2 = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA2)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    #muestra puntos, tiempo, el item y la letra
    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_BLANCO)
    ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1,COLOR_BLANCO)
    ren3 = defaultFontMUYGRANDE.render(letra if letra=="ñ" else letra.upper(), 1, COLOR_BLANCO)
    ren4 = defaultFont.render("CONTINUAR: 'S'",1,COLOR_ROJO)
    ren5 = defaultFont.render("FINALIZAR: 'ESC'",1,COLOR_ROJO)

    screen.blit(ren1, (ANCHO - 120, 10))
    screen.blit(ren2, (00, 10))
    screen.blit(ren3, (ANCHO//2-TAMANO_LETRA_GRANDE, 10))
    screen.blit(ren4, (10, 570))
    screen.blit(ren5, (ANCHO-200, 570))

    y=100
    for palabra in items:
        screen.blit(defaultFont2.render(palabra, 1, COLOR_BLANCO), (10, y))
        y=y+TAMANO_LETRA_GRANDE*2

    y=100
    i=0
    for palabra in eleccionUsuario:
        screen.blit(defaultFont2.render(palabra, 1, COLOR_VERDE if validacion[i]==1 else COLOR_ROJO), (ANCHO-510, y))
        y=y+TAMANO_LETRA_GRANDE*2
        i=i+1

    y=100
    for palabra in eleccioncompu:
        screen.blit(defaultFont2.render(palabra, 1, COLOR_AZUL), (ANCHO-290, y))
        y=y+TAMANO_LETRA_GRANDE*2

def dibujarResultado(screen,listaResultados,promedio):
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    #muestra puntos,aciertos , errores
    ren1 = defaultFontGRANDE.render("Puntos" , 1, COLOR_BLANCO)
    ren2 = defaultFontGRANDE.render("Aciertos" , 1, COLOR_BLANCO)
    ren3 = defaultFontGRANDE.render("Errores" ,1,COLOR_BLANCO)
    ren4 = defaultFontGRANDE.render("Tiempo Promedio   "+str(promedio)+" seg.",1,COLOR_ROJO if promedio > 30 else COLOR_VERDE)
    ren5 = defaultFontMUYGRANDE.render("FIN DEL JUEGO!",1,(255,0,0))

    screen.blit(ren1, (100, 150))
    screen.blit(ren2, (100, 225))
    screen.blit(ren3, (100, 300))
    screen.blit(ren4, (100, 375))
    screen.blit(ren5, (300, 500))

    y=150
    for i in range(len(listaResultados)-2):
        screen.blit(defaultFontGRANDE.render(listaResultados[i], 1, COLOR_BLANCO), (375, y))
        y=y+75
