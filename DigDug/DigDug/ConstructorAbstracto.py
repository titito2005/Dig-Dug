import pygame

from abc import ABC, abstractmethod

from Laberinto import Laberinto
from ObjetoLaberinto import ObjetoLaberinto
from BloqueDestructible import BloqueDestructible
from BloqueIndestructible import BloqueIndestructible
from Objetivo import Objetivo


class ConstructorAbstracto(ABC):
    '''Clase abstracta para los constructores de laberintos (aleatorio y por archivo de texto)'''

    def __init__(self):
        super().__init__()
        self.numCol = 0
        self.numFila = 0
        self.tamanoCuadro = 0

    @abstractmethod
    def crearLaberinto(self, cols, filas, tamanoBloque, bloqueDes, bloqueInd, bloqueVac, objetivo, poder, nivel = "nivel1"): 
        '''Crea el laberinto
        
        Parametros: 
        cols    (int): Numero de columnas de la matriz del laberinto
        filas   (int): Numero de filas de la matriz del laberinto
        tamanoBloque    (int): Tamaño de cada uno de los bloques
        bloqueDes   (BloqueDestructible): Bloque destructible del laberinto
        bloqueInd   (BloqueIndestructible): Bloque indestructible del laberinto
        bloqueVac   (BloqueIndestructible): Bloque vacío del laberinto
        objetivo    (ObjetoLaberinto): Objetivo del laberinto
        poder   (ObjetoLaberinto): Bloque de poder para el personaje
        nivel   (string): [Default = nivel1] Indica la dirección del archivo de texto para generar el laberinto.

        Retorno:

        Laberinto: Retorna el laberinto creado con los parámetros dados.
        '''
        pass
    
    @abstractmethod
    def crearObjetivo(self, posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo):
        '''Crea un objetivo en el laberinto
        
        Parametros:
        posx    (int): Posicion en x del objetivo
        posy    (int): Posicion en y del objetivo
        col     (int): Número de columna del objetivo en la matriz del laberinto
        fila    (int): Número de fila del objetivo en la matriz del laberinto
        tamano  (int): Tamano del bloque del objetivo
        nombre  (string): Nombre del objetivo
        ubicacionArchivo    (string): Ubicacion en donde se encuentra la imagen del objetivo
        nombreArchivo   (string): Nombre de la imagen del objetivo
        
        Retorno:
        ObjetoLaberinto: Retorna un objeto laberinto que representa el objetivo creado con los parametros dados
        '''
        pass

    @abstractmethod
    def crearBloque(self, posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo, resistencia = 0, destructible = False):
        '''Crea un bloque en el laberinto
        
        Parametros:
        posx    (int): Posición en x del bloque
        posy    (int): Posición en y del bloque
        col     (int): Numero de columna del bloque en la matriz del laberinto
        fila    (int): Numero de fila del bloque en la matriz del laberinto
        tamano  (int): Tamano del bloque
        nombre  (string): Nombre del bloque
        ubicacionArchivo    (string): Ubicacion en donde se encuentra la imagen del bloque
        nombreArchivo   (string): Nombre de la imagen del bloque
        resistencia     (int): [Default = 0] Indica la resistencia en caso de ser un bloque destructible
        destructible    (bool): [Default = False] Indica si es un bloque destructible
        
        Retorno:
        BloqueDestructibe - BloqueIndestructible: Puede retornar un BloqueDestructible o un BloqueIndestructible según los parametros dados
        '''
        pass
