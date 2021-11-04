import pygame as pg
import os
import random
import sys
from pygame.locals import*
from pygame.sprite import Group
from pygame.sprite import Sprite
from Personaje import Personaje
from Enemigo import Enemigo
from Jugador import Jugador
from Personaje_Extravelocidad import Personaje_Extravelocidad
from Personaje_Extravida import Personaje_Extravida
from Personaje_Inmunidad import Personaje_Inmunidad
from Entidad import Entidad

pg.init()

BLACK = (0,0,0)

size = (800, 800)
screen = pg.display.set_mode(size)
clock = pg.time.Clock()

#GENERADOR DE OBJETOS EN LA LISTA
#lista = []
#for i in range (60):
	#x = random.randint(0,800)
	#y = random.randint(0,500)
	#lista.append([x,y])

x=10;
y=20;

velocidad_x=0
valocidad_y=0

#MUESTRA O NO EL MOUSE

jugador = Jugador(10,20,3,10,10,'Graficos/Personaje#1','pixil-frame-0.png',800,800);
cont=0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                jugador.move(-1,0)
            if event.key == pg.K_RIGHT:
                jugador.move(1,0)
            if event.key == pg.K_UP:
                jugador.move(0,-1)
            if event.key == pg.K_DOWN:
                jugador.move(0,1)
                
        if event.type ==pg.KEYUP:
            if event.key == pg.K_LEFT:
                pass
            if event.key == pg.K_RIGHT:
                pass
            if event.key == pg.K_UP:
                pass
            if event.key == pg.K_DOWN:
                pass
    #print(cont)
    cont = cont+1
    
    if(cont==300):
        print("Entre")
        jugador= Personaje_Extravelocidad(jugador, 50, 50)
        
        
    screen.fill(BLACK)

    screen.blit(jugador.getImage(), (jugador.getRectX(), jugador.getRectY()))

    pg.display.flip()
    clock.tick(60)