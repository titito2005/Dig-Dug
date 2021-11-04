#CLASE ENEMIGO, HEREDA DE PERSONAJE
import pygame as pg
import pygame.font as font
import os
import pygame
import sys
from Personaje import Personaje

class Enemigo(Personaje):
    '''Clase Enemigo que hereda de Personaje'''
    
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
        self.cambioX = 1
        Personaje.__init__(self,posx,posy, valor, velX, velY, ubicacionArchivo, nombreArchivo, ancho, largo,imagenBala)

    def update(self):
        self.move(self.cambioX,0)
        if self.rect.x >= self.largoVentana - 51:
            self.cambioX = -1
        if self.rect.x <= 0:
            self.cambioX = 1

    def colisionConJugador(self,jugador):
        jugador.vida = jugador.vida -10

    def colisionBala(self,bala):  
        
        bala.morir()
        self.morir()

        