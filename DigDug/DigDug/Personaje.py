#CLASE PERSONAJE, HEREDA DE ENTIDAD
import pygame as pg
import pygame.font as font
import os
import pygame
import sys
from Entidad import Entidad
from Bala import balaMovimiento
class Personaje(Entidad):
    '''Clase Personaje que hereda de Entidad'''
    vida=0
    velocidadX=0
    velocidadY=0
    anchoVentana=0
    largoVentana=0
        
    def __init__(self,posx,posy,valor, velX, velY, ubicacionArchivo, nombreArchivo, ancho, largo,imagenBala):
        '''
        Descripcion:
        Constructor de la clase personaje
        
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
        Entidad.__init__(self,posx,posy, ubicacionArchivo, nombreArchivo)
        self.vida=valor
        self.velocidadX=velX
        self.velocidadY=velY
        self.anchoVentana=ancho
        self.largoVentana=largo
        self.imagenBala=imagenBala
    
    def definirVida(self,valor):
        '''
        Descripcion:
        Asigna nueva vida al personaje
        
        Parámetros:
        valor (int): nueva vida del personaje
        
        Retorno:
    
        '''
        self.vida=valor
    
    def getVida(self):
        '''
        Descripcion:
        Retorna la vida del personaje
        
        Parámetros:
        
        Retorno:
        self.vida: vida actual del personaje
        '''
        return self.vida
        
    def resteVida(self, cont):
        '''
        Descripcion:
        Resta vida al personaje
        
        Parámetros:
        cont (int): cantidad de vida a restar
        
        Retorno:
        sel.vida: vida actual del personaje
        '''
        self.vida= self.vida-cont
        if(self.vida<=0):
            morir()
            
        return self.vida
        
    def resteVida(self):
        '''
        Descripcion:
        Resta una vida al personaje
        
        Parámetros:
        
        Retorno:
        sel.vida: vida actual del personaje
        '''
        self.vida= self.vida-1
        return self.vida
        
    def asiganrVelocidadY(self, valor):
        '''
        Descripcion:
        Asigna una nueva velocidad en y al personaje
        
        Parámetros:
        valor (int): nueva velocidad en y
        
        Retorno:

        '''
        self.velocidadY = valor
    
    def asignarVelocidadX(self, valor):
        '''
        Descripcion:
        Asigna una nueva velocidad en x al personaje
        
        Parámetros:
        valor (int): nueva velocidad en x
        
        Retorno:

        '''
        self.velocidadX = valor
        
    def getVelocidadX(self):
        '''
        Descripcion:
        Retorna la velocidad en x
        
        Parámetros:
        
        Retorno:
        self.velocidadX: velocidad en x del personaje
        '''
        return self.velocidadX
        
    def getVelocidadY(self):
        '''
        Descripcion:
        Retorna la velocidad en y
        
        Parámetros:
        
        Retorno:
        self.velocidadY: velocidad en y del personaje
        '''
        return self.velocidadY
    
    def move(self,changeX,changeY):
        '''
        Descripcion:
        Mueve el persona a otra posición
        
        Parámetros:
        changeX (int): nueva posición en x
        changeY (int): nueva posición en y
        
        Retorno:

        '''
        self.rect.x += round(self.velocidadX * changeX) #Se agrega metodo round, para evitar warning de truncamiento implicito en la funcion "blit"
        self.rect.y += round(self.velocidadY * changeY)

        if self.rect.x >= self.largoVentana: #AGREGUE ESE -50 PORQUE LLEGABA A UN EXTREMO DEL MAPA SIN USO
            self.rect.x -= self.velocidadX * changeX

        if self.rect.x < 0:
            self.rect.x = 0
       
        if self.rect.y > 950: 
            self.rect.y = 950

        if self.rect.y >= self.anchoVentana:
            self.rect.y -= self.velocidadY * changeY
    
    def disparar(self,posx,posy,velocidadBala):
        '''
        Descripcion:
        Ataque del personaje
        
        Parámetros:
        
        Retorno:

        '''
        rotacion = self.getRotacion()
        nuevaBala=balaMovimiento(posx,posy,self.imagenBala,velocidadBala,rotacion)
        entidades = self.groups()[0]
        entidades.add(nuevaBala)

    #self.listaDisparo.append(nuevaBala)
    def getRotacion(self):
        resultado=0
        if self.image==self.imageIzquierda:
            resultado=1
        elif self.image==self.imageAbajo:
            resultado=2
        elif self.image==self.imageArriba:
            resultado=3
        return resultado
            
        
    
