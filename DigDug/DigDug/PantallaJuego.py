import pygame
class PantallaJuego():
    def __init__(self,anchoVentana,alturaVentana):
        '''Inicializa la ventana de juego
        Parametros:
        anchoVentana    (int): Indica el ancho de la ventana de juego
        alturaVentana    (int): Indica la altura de la ventana de juego
        '''
        self.ancho = anchoVentana
        self.altura = alturaVentana
        self.ventana = pygame.display.set_mode((self.ancho, self.altura))
        
    def dibujarElementos(self, elementos):
        '''Dibuja la lista de entidades en la pantalla de juego
        Parametros:
        elementos   (lista de entidades): Lista de entidades que se van a dibujar en la pantalla
        '''
        for entidad in elementos:
            self.ventana.blit(entidad.getImage(), (entidad.getRectX(), entidad.getRectY()))
    
    def actualizarPantalla(self):
        '''Actualiza la pantalla de juego para reflejar las nuevas modificaciones'''
        pygame.display.flip()
