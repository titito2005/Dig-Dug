import sys
import pygame
import os

from ConstructorAbstracto import *

class ConstructorArchivoTexto(ConstructorAbstracto):
    '''Construye un laberinto basandose en un archivo de texto.
    El archivo de texto debe contener los siguientes simbolos:
        -   representa vacio
        #   representa bloque destructible
        @   representa bloque indestructible
        %   representa un objetivo
        *   representa un poder
    '''
      
    def crearBloque(self, posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo, destructible = False, resistencia = 0):
        '''Crea un nuevo bloque en el laberinto actual
        
        Parametros:
        posx    (int): Posición en x del bloque
        posy    (int): Posición en y del bloque
        col     (int): Número de columna del bloque en la matriz del laberinto
        fila    (int): Número de fila del bloque en la matriz del laberinto
        tamano  (int): Tamano del bloque
        nombre  (string): Nombre del bloque
        ubicacionArchivo    (string): Ubicación en donde se encuentra la imagen del bloque
        nombreArchivo   (string): Nombre de la imagen del bloque
        resistencia     (int): [Default = 0] Indica la resistencia en caso de ser un bloque destructible
        destructible    (bool): [Default = False] Indica si es un bloque destructible
        
        Retorno:
        BloqueDestructibe - BloqueIndestructible: Puede retornar un BloqueDestructible o un BloqueIndestructible según los parametros dados
        '''

        if destructible:
            bloque = BloqueDestructible(posx, posy, col, fila, tamano, nombre, resistencia, ubicacionArchivo, nombreArchivo)
        else:
            bloque = BloqueIndestructible(posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo)

        return bloque
            

    def crearObjetivo(self, posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo):
        ''' Crea un nuevo Objetivo en el laberinto
        
        Parametros:
        posx    (int): Posición en x del objetivo
        posy    (int): Posición en y del objetivo
        col     (int): Número de columna del objetivo en la matriz del laberinto
        fila    (int): Número de fila del objetivo en la matriz del laberinto
        tamano  (int): Tamano del bloque del objetivo
        nombre  (string): Nombre del objetivo
        ubicacionArchivo    (string): Ubicación en donde se encuentra la imagen del objetivo
        nombreArchivo   (string): Nombre de la imagen del objetivo
        
        Retorno:
        ObjetoLaberinto: Retorna un objeto laberinto que representa el objetivo creado con los parametros dados
        '''

        objetivo = Objetivo( posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo)
        return objetivo

    def cargarLaberinto(self, nombreArchivo, laberinto, bloqueDes, bloqueInd, bloqueVac, objetivo, poder):
        '''Recorre el archivo de texto y genera los bloques correspondientes
        
        Parametros: 
        nombreArchivo    (string): Nombre del archivo de texto que contiene el laberinto
        laberinto   (Laberinto): Laberinto en el cual se van a cargar los valores del archivo de texto
        bloqueDes   (BloqueDestructible): Bloque destructible del laberinto
        bloqueInd   (BloqueIndestructible): Bloque indestructible del laberinto
        bloqueVac   (BloqueIndestructible): Bloque vacío del laberinto
        objetivo    (ObjetoLaberinto): Objetivo del laberinto
        poder   (ObjetoLaberinto): Bloque de poder para el personaje
        '''
        if (not os.path.isfile(nombreArchivo)):
            return False

        archivo = open(nombreArchivo, "r")
        data = archivo.read().split("\n") 

        x, y = 0, 0
        fil = 0
        for fila in data:
            col = 0
            for char in fila:
                if char == "#":
                    #Bloque destructible
                    bloqueDes = self.crearBloque(x, y, col, fil, self.tamanoCuadro, "BloqueDestructible", bloqueDes.ubicacionArchivo, bloqueDes.nombreArchivo, True, 1)
                    laberinto.cambiarMatriz(bloqueDes, fil, col)

                elif char == "@":
					#Bloque indestructible
                    bloqueIndes = self.crearBloque(x, y, col, fil, self.tamanoCuadro, "BloqueIndestructible", bloqueInd.ubicacionArchivo, bloqueInd.nombreArchivo)
                    laberinto.cambiarMatriz(bloqueIndes, fil, col)

                elif char == "%":
					#Objetivo
                    objetivo = self.crearObjetivo(x, y, col, fil, self.tamanoCuadro, "Objetivo", objetivo.ubicacionArchivo, objetivo.nombreArchivo)
                    laberinto.cambiarMatriz(objetivo, fil, col)

                elif char == "-":
                    vacio = self.crearBloque(x, y, col, fil, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    laberinto.cambiarMatriz(vacio, fil, col)

                elif char == "*":
                    poder = self.crearBloque(x, y, col, fil, self.tamanoCuadro, "Poder", poder.ubicacionArchivo, poder.nombreArchivo)
                    laberinto.cambiarMatriz(poder, fil, col)

                x += self.tamanoCuadro
                col += 1 
            x = 0
            y += self.tamanoCuadro
            fil += 1

        archivo.close()
        return True

    def crearLaberinto(self, cols, filas, tamanoBloque, bloqueDes, bloqueInd, bloqueVac, objetivo, poder, nivel = "nivel1"):
        '''Carga el laberinto desde un archivo de texto
        
        Parametros: 
        cols    (int): Número de columnas de la matriz del laberinto
        filas   (int): Número de filas de la matriz del laberinto
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

        if (not os.path.isfile(nivel)):
            print("No se encuentra el archivo " , nivel)
            sys.exit("[Error en el nombre del archivo del laberinto]")

        archivo = open(nivel, "r")
        data = archivo.read().split("\n") 

        self.numCol = cols
        self.numFila = filas
        self.tamanoCuadro = tamanoBloque

        laberinto = Laberinto(self.numCol, self.numFila, self.tamanoCuadro)

        cargado = self.cargarLaberinto(nivel, laberinto, bloqueDes, bloqueInd, bloqueVac, objetivo, poder)
        
        if not cargado:
            sys.exit("[Error al cargar el laberinto, revise el formato del archivo]")

        return laberinto

        
