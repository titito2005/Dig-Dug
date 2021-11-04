from ObjetoLaberinto import ObjetoLaberinto

class BloqueIndestructible(ObjetoLaberinto):
    '''Hereda de la clase ObjetoLaberinto y representa un bloque que no puede ser destruido'''

    def __init__(self, posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo):
        super().__init__(posx, posy, col, fila, tamano, nombre, ubicacionArchivo, nombreArchivo)
        self.pasable = False

    def getPasable(self):
        return self.pasable

    def setPasable(self, nuevoPasable):
        self.pasable = nuevoPasable

    def colisionConJugador(self,jugador):
        if self.getnombre() == "bloqueVacio" or self.getnombre() == "Poder":
            pass
        else:
            rotacion = jugador.getRotacion()
            if rotacion == 0:
                jugador.move(jugador.x-1, jugador.y)
            if rotacion == 1:
                jugador.move(jugador.x+1, jugador.y)
            if rotacion == 2:
                jugador.move(jugador.x, jugador.y-1)
            if rotacion == 3:
                jugador.move(jugador.x, jugador.y+1)
            pass



