import pygame
import sys
from Laberinto import Laberinto
from PantallaJuego import PantallaJuego
from Jugador import Jugador
from Enemigo import Enemigo
from Bala import bala
from BloqueDestructible import BloqueDestructible
from BloqueIndestructible import BloqueIndestructible
from Objetivo import Objetivo
from Bala import balaMovimiento
class Controlador():

    def __init__(self):
        '''Inicializa las variables del controlador'''
        pygame.init()
        self.entidades = pygame.sprite.Group()
        self.ventanaJuego = None
        self.laberinto = None
        self.jugador = None


    def ejecutarMenu(self):
        pass

    def crearLaberinto(self, filas, columnas, tamanoCuadro):
        '''Inicia el laberinto del Controlador
        Parametros:
        filas   (int): Cantidad de filas del laberinto que se quiere crear
        columnas    (int): Cantidad de columnas del laberinto que se quiere crear
        tamanoCuadro    (int): Tamano de los cuadros que conforman el laberinto
        '''
        self.laberinto = Laberinto(filas, columnas, tamanoCuadro)

    def setLaberinto(self, laberinto):
        '''Asigna un nuevo laberinto al Controlador
        Parametros:
        laberinto   (laberinto): Es el nuevo laberinto que se le quiere asignar al Controlador'''
        self.laberinto = laberinto

    def getLaberinto(self):
        '''Retorna el laberinto del controlador'''
        return self.laberinto

    def getEntidades(self):
        '''Retorna el grupo de entidades del Controlador'''
        return self.entidades

    def crearVentanaJuego(self,anchoVentana, alturaVentana):
        '''Inicializa la ventana del juego
        Parametros:
        anchoVentana    (int): Ancho de la ventana de juego
        alturaVentana   (int): Ancho de la ventana de juego
        '''
        self.ventanaJuego = PantallaJuego(anchoVentana,alturaVentana)
    
    def agregarEntidad(self, entidadNueva):
        '''Agrega una entidad al grupo de entidades del Controlador'''
        self.entidades.add(entidadNueva)


    def crearEnemigo(self, posx, posy, velX, velY, ubicacionArchivo, nombreArchivo):
        '''Crea un nuevo enemigo
        Parametros:
        posx    (int): Posicion en el eje x del enemigo
        posy    (int): Posicion en el eje y del enemigo
        vida    (int): Vida del enemigo
        velX    (int): Velocidad en el eje x del enemigo
        velY    (int): Velocidad en el eje y del enemigo
        ubicacionArchivo    (string): Ubicacion de la imagen del enemigo
        nombreArchivo   (string): Nombre de la imagen del enemigo

        Retorno:
        enemigoNuevo    (Enemigo): Retorna el nuevo enemigo
        '''
        enemigoNuevo = Enemigo(posx,posy,velX,velY,ubicacionArchivo, nombreArchivo, self.ventanaJuego.ancho, self.ventanaJuego.altura)
        self.agregarEntidad(enemigoNuevo)
        return enemigoNuevo
    

    def crearJugador(self, posx, posy,vida, velX, velY, ubicacionArchivo, nombreArchivo,imagenBala):
        '''Crea un nuevo jugador
        Parametros:
        posx    (int): Posicion en el eje x del jugador
        posy    (int): Posicion en el eje y del jugador
        vida    (int): Vida del jugador
        velX    (int): Velocidad en el eje x del jugador
        velY    (int): Velocidad en el eje y del jugador
        ubicacionArchivo    (string): Ubicacion de la imagen del jugador
        nombreArchivo   (string): Nombre de la imagen del jugador

        Retorno:
        jugador    (Jugador): Retorna el nuevo jugador
        '''

        self.jugador = Jugador(posx,posy,vida,velX,velY,ubicacionArchivo, nombreArchivo, self.ventanaJuego.ancho, self.ventanaJuego.altura,imagenBala)
        self.agregarEntidad(self.jugador) 
        return self.jugador

    def crearEnemigo(self, posx, posy,vida, velX, velY, ubicacionArchivo, nombreArchivo,imagenBala):
        enemigoNuevo = Enemigo(posx,posy,vida,velX,velY,ubicacionArchivo, nombreArchivo, self.ventanaJuego.ancho, self.ventanaJuego.altura,imagenBala)
        self.agregarEntidad(enemigoNuevo)
        return enemigoNuevo

    def eliminarEntidad(entidad):
        '''Elimina una entidad
        Parametros:
        entidad     (entidad): Entidad que se quiere eliminar'''
        entidad.morir()

    def ejecutarJuego(self):
        '''Contiene el ciclo principal del juego'''
        if self.ventanaJuego is not None :
            done = False
            while not done:   
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                                pygame.quit()
                                sys.exit(0)

                self.ventanaJuego.ventana.fill((0,0,1))
                #Dibuja en la vista todas las entidades que se han creado
                if(self.laberinto is not None):
                    self.ventanaJuego.dibujarElementos(self.laberinto.objetos)

                self.ventanaJuego.dibujarElementos(self.entidades)
                self.ventanaJuego.actualizarPantalla()

                '''revisa las colisiones entre el jugador y el laberinto'''
                for entidad in self.laberinto.objetos:
                    if entidad != self.jugador:
                        if entidad.rect.colliderect(self.jugador) == True:
                            entidad.colisionConJugador(self.jugador)

                '''revisa las coliones entre el jugador y las demas entidades'''
                for entidad in self.entidades:
                    if entidad != self.jugador:
                        if entidad.rect.colliderect(self.jugador) == True:
                            entidad.colisionConJugador(self.jugador)

                for entidad in self.entidades:
                   
                    if type(entidad) is  balaMovimiento:
                        
                        for entidad2 in self.entidades:
                            
                            if entidad2.rect.colliderect(entidad) == True:
                                 
                                 
                                 entidad2.colisionBala(entidad)

                #'Le da vida' a todos las entidades que se han creado. Llama el metodo update de cada entidad
                self.entidades.update()



        else:
            print("Error: No existe una ventana para el juego.")

     
   