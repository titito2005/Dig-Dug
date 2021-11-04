import pygame as pg
import pygame.font as font
import os
import pygame
import sys
from Entidad import Entidad
class bala(Entidad):
    '''Clase abstracta para generar una bala'''
    
    def __init__(self):
        #print("Hola")
        pass

    def dibujar(self):
        #print("Disparo")
        pass

class balaMovimiento(bala):
    ''' Construye una bala con movimiento'''

    def __init__(self,posx,posy,imagenUsuario,velocidadBala,rotacion):
        '''Inicialza la bala con movimiento
        Parametros:
        posx   (int):posicion x para el rectangulo de la bala
        posy    (int):posicion y para el rectangulo de la bala
        imagenUsuario  (imagen): imagen del usuario que representa la bala en la pantalla
        velocidadBala  (int): velocidada en que la bala se mueve en la pantalla
        Retorno:
        void
        '''
        Entidad.__init__(self,posx,posy,"", imagenUsuario)
        
        pg.sprite.Sprite.__init__(self)
        self.velocidadDisparo=velocidadBala
        self.rect.top=posy
        self.rect.left=posx
        self.rotacion=rotacion
        if self.rotacion==0:
            self.image = self.imageDerecha
        elif self.rotacion==1:
            self.image = self.imageIzquierda
        elif self.rotacion==2:
            self.image = self.imageAbajo
        elif self.rotacion==3:
            self.image = self.imageArriba


    def trayectoria(self):
        '''Actauliza la posicion de la bala para que esta se meuva
        Parametros:
        N/A
        Retorna:
        void
        '''
        if self.rotacion==0:
            self.rect.left=self.rect.left+self.velocidadDisparo
        elif self.rotacion==1:
            self.rect.left=self.rect.left-self.velocidadDisparo
        elif self.rotacion==2:
            self.rect.top=self.rect.top+self.velocidadDisparo
        elif self.rotacion==3:
            self.rect.top=self.rect.top-self.velocidadDisparo


    def update(self):
        self.trayectoria()
    

class balaSinMovimieto(bala):
    '''Crea una bala que no tiene movimiento'''
  
    def __init__(self,posx,posy,imagenUsuario):
        '''Inicializa la bala sin movimiento
        posx (int): posicion en x para el rectangulo de la bala
        posy (int): posicion en y para el rectangulo de la bala
        imagenUsuario (imagen): imagen del usuario que representa la bala en la panatlla
        '''
        pg.sprite.Sprite.__init__(self)
        self.imagenUsuario=imagenUsuario
        self.rect=self.imagenUsuario.get_rect()
        self.rect.top=posy
        self.rect.left=posx
    

    


