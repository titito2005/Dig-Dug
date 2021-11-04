from ConstructorAbstracto import *
import random

class ConstructorAleatorio(ConstructorAbstracto):
    '''Construye un laberinto de manera aleatoria'''
    
    def crearBloque(self, posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo, destructible = False ,resistencia = 0 ):
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
        '''Crea un nuevo Objetivo en el laberinto
        
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
    
    #Se ignora el parametro nivel
    def crearLaberinto(self, cols , filas, tamanoBloque, bloqueDes, bloqueInd, bloqueVac, objetivo, poder,nivel='nivel1'):
        '''Crea un laberinto aleatorio
        
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

        self.numCol = cols
        self.numFila = filas
        self.tamanoCuadro = tamanoBloque
        laberinto = Laberinto(self.numFila, self.numCol, self.tamanoCuadro)
        laberinto.rellenarLaberinto(bloqueDes)

        for fila in range(laberinto.filas):
            for col in range(laberinto.columnas):
                patronID = random.randint(1,30)
                if patronID == 1 and col > 1 and col < laberinto.columnas - 2:
                    bloqueVacio = self.crearBloque(0, 0, col, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio2 = self.crearBloque(0, 0, col-1, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio3 = self.crearBloque(0, 0, col-2, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio4 = self.crearBloque(0, 0, col+1, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio5 = self.crearBloque(0, 0, col+2, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)

                    laberinto.cambiarMatriz(bloqueVacio, fila, col)
                    laberinto.cambiarMatriz(bloqueVacio2, fila, col-1)
                    laberinto.cambiarMatriz(bloqueVacio3, fila, col-2)
                    laberinto.cambiarMatriz(bloqueVacio4, fila, col+1)
                    laberinto.cambiarMatriz(bloqueVacio5, fila, col+2)
                    
                elif patronID == 2 and fila > 1  and fila < laberinto.filas - 2:
                    bloqueVacio = self.crearBloque(0, 0, col, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio2 = self.crearBloque(0, 0, col, fila-1, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio3 = self.crearBloque(0, 0, col, fila-2, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio4 = self.crearBloque(0, 0, col, fila+1, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio5 = self.crearBloque(0, 0, col, fila+2, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                         
                    laberinto.cambiarMatriz(bloqueVacio, fila, col)
                    laberinto.cambiarMatriz(bloqueVacio2, fila-1, col)
                    laberinto.cambiarMatriz(bloqueVacio3, fila-2, col)
                    laberinto.cambiarMatriz(bloqueVacio4, fila+1, col)
                    laberinto.cambiarMatriz(bloqueVacio5, fila+2, col)
                    
                elif patronID == 3 and col != 0 and fila != 0  and col < laberinto.columnas - 1 and fila < laberinto.filas - 1:
                    bloqueVacio = self.crearBloque(0, 0, col, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio2 = self.crearBloque(0, 0, col+1, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio3 = self.crearBloque(0, 0, col-1, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio4 = self.crearBloque(0, 0, col, fila+1, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio5 = self.crearBloque(0, 0, col, fila-1, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)

                    laberinto.cambiarMatriz(bloqueVacio, fila, col)
                    laberinto.cambiarMatriz(bloqueVacio2, fila, col+1)
                    laberinto.cambiarMatriz(bloqueVacio3, fila, col-1)
                    laberinto.cambiarMatriz(bloqueVacio4, fila+1, col)
                    laberinto.cambiarMatriz(bloqueVacio5, fila-1, col)

                elif patronID == 4 and fila > 1  and col < laberinto.columnas - 1:
                    bloqueVacio = self.crearBloque(0, 0, col, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio2 = self.crearBloque(0, 0, col+1, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio4 = self.crearBloque(0, 0, col, fila-2, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio5 = self.crearBloque(0, 0, col, fila-1, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                         
                    laberinto.cambiarMatriz(bloqueVacio, fila, col)
                    laberinto.cambiarMatriz(bloqueVacio2, fila, col+1)
                    laberinto.cambiarMatriz(bloqueVacio4, fila-1, col)
                    laberinto.cambiarMatriz(bloqueVacio5, fila-2, col)

                elif patronID == 5 and col > 1 and fila < laberinto.filas - 2:
                    bloqueVacio = self.crearBloque(0, 0, col, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio2 = self.crearBloque(0, 0, col-1, fila, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio4 = self.crearBloque(0, 0, col, fila+2, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)
                    bloqueVacio5 = self.crearBloque(0, 0, col, fila+1, self.tamanoCuadro, "bloqueVacio", bloqueVac.ubicacionArchivo, bloqueVac.nombreArchivo)

                    laberinto.cambiarMatriz(bloqueVacio, fila, col)
                    laberinto.cambiarMatriz(bloqueVacio2, fila, col-1)
                    laberinto.cambiarMatriz(bloqueVacio4, fila+1, col)
                    laberinto.cambiarMatriz(bloqueVacio5, fila+2, col)

        #Se agregan los bloques indestructibles
        for fila in range(laberinto.filas):
            for col in range(laberinto.columnas):
                cambiar = random.randint(1, 20)
                if cambiar < 5 and laberinto.matriz[fila][col].getnombre() != "bloqueVacio":
                    laberinto.matriz[fila][col].image = bloqueInd.image

        #Poner objetivo
        objetoCol = 0
        objetoFila = 0
        valido = False
        while not valido:
            objetoCol = random.randint(3, laberinto.columnas-1)
            objetoFila = random.randint(3, laberinto.filas-1)
            if laberinto.matriz[objetoFila][objetoCol].getnombre() != "bloqueVacio":
                laberinto.matriz[objetoFila][objetoCol].image = objetivo.image
                laberinto.matriz[objetoFila][objetoCol].setNombre("Objetivo")
                valido = True

        #Poner poder
        poderCol = 0
        poderFila = 0
        valido = False
        while not valido:
            poderCol = random.randint(3, laberinto.columnas-1)
            poderFila = random.randint(3, laberinto.filas-1)
            if laberinto.matriz[poderFila][poderCol].getnombre() == "bloqueVacio":
                laberinto.matriz[poderFila][poderCol].image = poder.image
                laberinto.matriz[poderFila][poderCol].setNombre("Poder")
                valido = True
        


        return laberinto






