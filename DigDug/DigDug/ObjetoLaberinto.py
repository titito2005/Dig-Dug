from Entidad import Entidad
from Jugador import Jugador

class ObjetoLaberinto(Entidad):
    '''Hereda de la clase Entidad y representa cualquier objeto en el laberinto'''
        
    def __init__(self,posx,posy,col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo):
        Entidad.__init__(self,posx,posy, ubicacionArchivo, nombreArchivo)
        self.columna = col
        self.fila = fila
        self.TamanoMax = tamano
        self.nombre = nombre
        self.ubicacionArchivo=ubicacionArchivo
        self.nombreArchivo=nombreArchivo

    def getnombre(self):
        '''Retorna el nombre del objetoLaberinto actual'''
        return self.nombre

    def getTamanoMax(self):
        '''Retorna el tamaño del objetoLaberinto actual'''
        return self.TamanoMax

    def getColumna(self):
        '''Retorna la columna del objetoLaberinto actual en la matriz de su laberinto correspondiente'''
        return self.columna

    def getFila(self):
        '''Retorna la fila del objetoLaberinto actual en la matriz de su laberinto correspondiente'''
        return self.fila

    def setFila(self, nuevaFila):
        '''Asigna un nuevo valor de fila para el objetoLaberinto actual en la matriz de su laberinto correspondiente
        
        Parametros:
        nuevaFila (int): Valor de la nueva fila'''
        self.fila = nuevaFila

    def setCol(self, nuevaCol):
        '''Asigna un nuevo valor de columna para el objetoLaberinto actual en la matriz de su laberinto correspondiente
        
        Parametros:
        nuevaCol (int): Valor de la nueva columna'''
        self.columna = nuevaCol

    def setNombre(self, nuevoNombre):
        '''Asigna un nuevo nombre al objetoLaberinto actual
        
        Parametros:
        nuevoNombre (string): Nuevo nombre del objetoLaberinto'''
        self.nombre = nuevoNombre