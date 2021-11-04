from ObjetoLaberinto import ObjetoLaberinto
from BloqueDestructible import BloqueDestructible
from BloqueIndestructible import BloqueIndestructible
from Objetivo import Objetivo
from Controlador import Controlador
from Entidad import Entidad
import pygame
import sys
import os
import pygame.font as font
import pygame
import sys
import random
import threading
import time

from ConstructorAleatorio import ConstructorAleatorio
from ConstructorArchivoTexto import ConstructorArchivoTexto

digdug = Controlador()
digdug.crearVentanaJuego(640,640)
digdug.crearLaberinto(10,10,64)
cielo = ObjetoLaberinto(0,0,0,0,0,"bloque1", 'Graficos/Laberinto', 'Cielo.png')
laberintoDigDug = digdug.getLaberinto()
laberintoDigDug.rellenarLaberinto(cielo)
e1 = digdug.crearJugador(0,0,100,25,25,'Graficos/Personaje#1', 'pixil-frame-0.png',"Graficos/Bala/BalaDerecha.png") 
enemigos = []
for cont in range(5):
    enemigos.append(digdug.crearEnemigo(400,cont * 50,100,1,1,'Graficos/Enemigo#1', 'pixil-frame-0.png',"Graficos/Bala/BalaDerecha.png"))
    



#Pruebas de laberinto aleatorio:
#constructor = ConstructorAleatorio()
#bloqueDes = BloqueDestructible(0, 0, 0, 0, 0, "Tierra", 2, "Graficos/Laberinto", "Tierra.png")
#bloqueInd = BloqueIndestructible(0, 0, 0, 0, 0, "Cielo", "Graficos/Laberinto", "Cielo.png")
#bloqueVac = BloqueIndestructible(0, 0, 0, 0, 0, "Vacio", "Graficos/Laberinto", "Vacio.png")
#objetivo = Objetivo(0, 0, 0, 0, 0, "Tesoro", "Graficos/Laberinto", "Tesoro.png")
#poder = BloqueDestructible(0,0,0,0,0,"Poder", 0, "Graficos/Laberinto", "Poder.png")
#laberinto2 = constructor.crearLaberinto(10,10,65,bloqueDes,bloqueInd,bloqueVac,objetivo, poder)
#digdug.setLaberinto(laberinto2)

#Pruebas de laberinto Archivo
constructor = ConstructorArchivoTexto()
bloqueDes = BloqueDestructible(0, 0, 0, 0, 0, "Tierra", 2, "Graficos/Laberinto", "Tierra.png")
bloqueInd = BloqueIndestructible(0, 0, 0, 0, 0, "Cielo", "Graficos/Laberinto", "Indestructible.png")
bloqueVac = BloqueIndestructible(0, 0, 0, 0, 0, "Vacio", "Graficos/Laberinto", "Vacio.png")
objetivo = Objetivo(0, 0, 0, 0, 0, "Tesoro", "Graficos/Laberinto", "Tesoro.png")
poder = BloqueDestructible(0,0,0,0,0,"Poder", 0, "Graficos/Laberinto", "VacioPoder.png")

laberinto3 = constructor.crearLaberinto(10, 10, 65, bloqueDes, bloqueInd, bloqueVac, objetivo, poder, "Niveles/NivelPrueba.txt")
digdug.setLaberinto(laberinto3)

digdug.ejecutarJuego()
