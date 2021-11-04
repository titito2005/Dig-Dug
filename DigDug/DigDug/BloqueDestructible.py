from ObjetoLaberinto import ObjetoLaberinto

class BloqueDestructible(ObjetoLaberinto):
    '''Hereda de la clase ObjetoLaberinto y representa un bloque que puede ser destruido'''
    
    def __init__(self, posx, posy, col, fila, tamano, nombre, resistencia, ubicacionArchivo, nombreArchivo):
        super().__init__(posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo)
        self.resistencia = resistencia

    def getResistencia(self):
        '''Retorna la resistencia del bloque destructible actual'''
        return self.resistencia

    def setResistencia(self, nuevaResistencia):
        '''Asigna un nuevo valor a la resistencia del bloque actual
        Parametros:
        nuevaResistencia    (int): Valor de la nueva resistencia que se le quiere asignar al bloque actual'''
        self.resistencia = nuevaResistencia

    def colisionConJugador(self,jugador):
        self.morir()



