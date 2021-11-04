from ObjetoLaberinto import ObjetoLaberinto

class Objetivo(ObjetoLaberinto):
    '''Hereda de la clase ObjetoLaberinto y representa un objetivo del juego'''
    def __init__(self, posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo):
        super().__init__(posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo)


