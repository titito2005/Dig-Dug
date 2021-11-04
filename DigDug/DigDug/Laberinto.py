import pygame
from ObjetoLaberinto import ObjetoLaberinto

class Laberinto():
    def __init__(self, filas, columnas, tamanoCuadro):
        '''Inicializa el laberinto con una cantidad de filas, columnas y el tamano de cada cuadro
        
        Parametros:
        filas   (int): Cantidad de filas del laberinto
        columnas    (int): Cantidad de columnas del laberinto
        tamanoCuadro    (int): Tamano del cada uno de los cuadros que conforman el laberinto
        '''

        self.filas = filas
        self.columnas = columnas
        self.tamanoCuadro = tamanoCuadro
        self.matriz = []
        for fila in range(self.filas):
            self.matriz.append([])
            for columna in range(self.columnas):
                self.matriz[fila].append(ObjetoLaberinto(0,0,0,0,0,None,"Graficos/Laberinto", "Tierra.png"))

        self.objetos = pygame.sprite.Group()
        self.objetos.add(self.matriz)

    def rellenarLaberinto(self,objetoRelleno):
        '''Rellena la matriz del laberinto con el objeto que se le envia por parametros
        Parametros:
        objetoRelleno (ObjetoLaberinto): Objeto con el cual se va a rellenar el laberinto

        '''
        for fila in range(self.filas):
            for columna in range(self.columnas):
                #Instancia una copia del objeto de Relleno | TO DO: Crear meotodo de copia generico en Entidad
                objetoNuevo = ObjetoLaberinto(0,0,objetoRelleno.columna,objetoRelleno.fila,objetoRelleno.TamanoMax,objetoRelleno.nombre, objetoRelleno.ubicacionArchivo, objetoRelleno.nombreArchivo)
                objetoNuevo.image = objetoRelleno.image

                self.cambiarMatriz(objetoNuevo, fila, columna)

    def cambiarMatriz(self, objetoNuevo, fila, columna):
        '''Modifica la posicion [fila][columna] de la matriz del laberinto, por el objeto que se envia por parametros
        Parametros:
        objetoNuevo (ObjetoLaberinto): Objeto con el cual se va a rellenar la posicion fila, columna del laberinto
        fila    (int): Fila en la matriz del nuevo objeto que se quiere agregar al laberinto
        columna     (int): Columna en la matriz del nuevo objeto que se quiere agregar al laberinto
        '''

        self.matriz[fila][columna].kill()
        objetoNuevo.rect.y = fila * self.tamanoCuadro
        objetoNuevo.rect.x = columna * self.tamanoCuadro
        self.matriz[fila][columna] = objetoNuevo
        self.objetos.add(objetoNuevo)

        
        




