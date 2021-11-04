#CLASE JUGADOR, HEREDA DE PERSONAJE
import pygame as pg
import pygame.font as font
import os
import pygame
import sys
from Personaje import Personaje

class Jugador(Personaje):
    '''Clase Jugador que hereda de Personaje'''
    
    def __init__(self,posx,posy,valor, velX, velY, ubicacionArchivo, nombreArchivo, ancho, largo,imagenBala):#Se define la posición en x y y de inicio, y la vida e inicio.
        '''
        Descripcion:
        Constructor de la clase Enemigo
        
        Parametros:
        posx (int): posicion en x para el inicio del personaje
        posy (int): posicion en y para el inicio del personaje
        valor (int): vida inicial del personaje
        velX (int): valocidad del movimiento en x
        velY (int): velocidad del moviemiento en y
        ubicacionArchivo (string): ubicacion en la que se obtiene la imagen principal
        nombreArchivo (string): nombre de la imagen inicial
        ancho (int): ancho de la ventana en la que se mueve
        largo (int): largo de la ventana en la que ser mueve
        
        Retorno:
        
        '''
        Personaje.__init__(self,posx,posy, valor, velX, velY, ubicacionArchivo, nombreArchivo, ancho, largo,imagenBala)
        pygame.key.set_repeat(100,50) 
    
    def update(self):
        if self.vida <= 0: 
            self.morir()
        for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.move(-1,0)
                           
                            self.image=self.imageIzquierda
                        if event.key == pygame.K_RIGHT:
                            self.move(1,0)
                            self.image=self.imageDerecha

                        if event.key == pygame.K_UP:
                            self.move(0,-1)
                            
                            self.image=self.imageArriba

                        if event.key == pg.K_DOWN:
                            self.move(0,1)
                            self.image = self.imageAbajo
                            
                        if event.key == pg.K_SPACE:
                            
                            x=self.rect.x
                            y=self.rect.y
                           
                            self.disparar(x,y,10)
                            print("disparar")
                            pass



                        if event.key == pygame.K_RETURN:#Pruebas para pantalla final del juego
                            done = True
                            finDelJuego(False,puntajeMostrar)
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)