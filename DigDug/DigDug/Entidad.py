#CLASE ENTIDAD
import pygame as pg
import os
import random
from pygame.locals import*
from pygame.sprite import Group
from pygame.sprite import Sprite

import pygame.font as font 
import pygame
import sys
import random
import threading
import time


class Entidad(pg.sprite.Sprite):
    '''Clase abstracta para la creación de entidades, con animación y sin animación '''
    x = 0
    y = 0
    cantImagenesMovimieto = 0
    cantImagenesMuerte = 0
    animacionMovimiento = []
    animacionMuerte = []   
    animacionActual = []
    image = None
    tamanoAnimacionActual = 0
    contadorAnimacion = 0 # indice de animacionActual
    tiempoTranscurrido = 0 
    velocidadAnimacion = 0 # velocidad de animacion
    animacionActivada = False
    eliminar = False
    numeroAnimacion = 0


    def __init__(self,posx,posy, ubicacionArchivo, nombreArchivo):
        '''
        Descripcion:
        Constructor de la clase entidad
        
        Parametros:
        posx (int): posicion en x para el inicio de la entidad
        posy (int): posicion en y para el inicio de la entidad
        ubicacionArchivo (string): ubicacion en la que se obtiene la imagen principal
        nombreArchivo (string): nombre de la imagen inicial
        
        Retorno:
        
        '''
        pygame.sprite.Sprite.__init__(self)
        self.imageDerecha=pg.image.load(os.path.join(ubicacionArchivo, nombreArchivo))
        self.image =  pg.image.load(os.path.join(ubicacionArchivo, nombreArchivo))
        self.imageIzquierda=pygame.transform.flip(self.imageDerecha, True, False)
        self.imageArriba=pygame.transform.rotate(self.imageDerecha,  90)
        self.imageAbajo= pygame.transform.rotate(self.imageDerecha, -90)
        self.image =self.imageDerecha
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.numeroAnimacion=0
        self.velocidadAnimacion = 3
        self.cantAnimacionMuerte=0

    def agregarAnimacionMovimiento(self, animacionNueva):
        '''
        Descripcion:
        Agrega un vector con la animación de movimiento a la entidad
        
        Parametros:
        animacionNueva (vector): Vector con las animaiones de movimiento
    
        Retorno:
        
        '''
        self.animacionMovimiento = animacionNueva
        self.animacionActivada = True

    def agregarAnimacionMuerte(self, animacionNueva):
        '''
        Descripcion:
        Agrega un vector con la animación de muerte a la entidad
        
        Parametros:
        animacionNueva (vector): Vector con las animaiones de muerte
    
        Retorno:
        
        '''
        self.animacionMuerte = animacionNueva
        self.animacionActivada = True
        self.eliminar=True

    def cambiarAnimacionMuerte(self):
        '''
        Descrición:
        Cambia la animación utilizada actualmente por la entidad por la animación de muerte
        
        Parametros:
    
        Retorno:
        
        '''
        self.animacionActual = self.animacionMuerte
        self.tamanoAnimacionActual = len(self.animacionActual)
        self.numeroAnimacion=0
        self.contadorAnimacion = 0

    def cambiarAnimacionMovimiento(self):
        '''
        Descripcion:
        Cambia la animación utilizada actualmente por la entidad por la animación de movimiento
        
        Parametros:
    
        Retorno:
        
        '''
        self.animacionActual=self.animacionMovimiento
        self.tamanoAnimacionActual = len(self.animacionActual)
        self.numeroAnimacion=0
        self.contadorAnimacion = 0

    def cambiarVelocidadAnimacion(self, tiempo):
        '''
        Descripcion:
        Cambia la velocidad con la que transcurre la animación en la entidad
        
        Parametros:
        tiempo (int): Indica la velocidad con la que la animación del personaje transcurre
    
        Retorno:
        
        '''
        self.velocidadAnimacion=tiempo

    def actualizarImagen(self):
        '''
        Descrición:
        Método que se encarga de actualizar la imagen de animación de la entidad
        
        Parametros:
    
        Retorno:
        
        '''
        if self.animacionActivada == True:
            if self.contadorAnimacion > self.velocidadAnimacion:
                self.contadorAnimacion = 0
                
                self.image = self.animacionActual[self.numeroAnimacion]
                self.numeroAnimacion = self.numeroAnimacion + 1
                
                if self.numeroAnimacion >= self.tamanoAnimacionActual:
                    self.numeroAnimacion = 0
    
                if self.eliminar==True:
                    self.morir()
            else:
                self.contadorAnimacion = self.contadorAnimacion + 1

    def getRectX(self):
        '''
        Descrición:
        Retorna la posición en x de la entidad
        
        Parametros:
    
        Retorno:
        self.rect.x: Retorna la posición actual en x
        '''
        return self.rect.x

    def getRectY(self):
        '''
        Descrición:
        Retorna la posición en y de la entidad
        
        Parametros:
    
        Retorno:
        self.rect.y: Retorna la posición actual en y
        '''
        return self.rect.y

    def getImage(self):
        '''
        Descripcion:
        Retorna la imagen actual de la entidad
        
        Parametros:
    
        Retorno:
        self.image: Retorna la imagen actual de la entidad
        '''
        return self.image

    def morir(self):
        '''
        Descripcion:
        Método que elimina la entidad de todos los grupos de sprites
        
        Parametros:
    
        Retorno:

        '''
        self.kill()

    def update(self):
        '''
        Descripcion:
        Método que actualiza el estado de la entidad
        
        Parametros:
    
        Retorno:

        '''
        pass
    def colisionConJugador(self, jugador):
        pass

    def colisionBala(self,bala):
        pass

	#entidad=Entidad(12,12,pg.image.load(os.path.join('Graficos/Personaje#1', 'pixil-frame-0.png')))
