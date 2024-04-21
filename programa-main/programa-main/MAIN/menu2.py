import pygame 
import sys
from pygame.locals import *


#pantalla tamaño
max_width = 1920
max_height = 1080
def scale_surface(surface, width, height):
    width, height = surface.get_size()
    scale = min(max_width / width, max_height / height)
    return pygame.transform.scale(surface, (int(width * scale), int(height * scale)))


pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Menu2')

nuevo_ancho_regresar = 300  # Cambia esto al ancho deseado para la imagen de regresar
nuevo_alto_regresar = 300 # Cambia esto al alto deseado para la imagen de regresar

# imagenes con escalas
directorio = "programa-main/imagenes"
fondo3 = scale_surface(pygame.image.load(f"{directorio}/fondo3.png"), 1920, 1080)
logincio = scale_surface(pygame.image.load(f"{directorio}/botonlog.png"), 1920, 1080)
regresar = scale_surface(pygame.image.load(f"{directorio}/regresar.png"), 1920, 1080)

#modificar regresar a un tamaño más pequeño
regresar = pygame.transform.scale(regresar, (nuevo_ancho_regresar, nuevo_alto_regresar))

#rect imagenes
recfondo3 = fondo3.get_rect(center=(960, 530 + 100))
reclogincio = logincio.get_rect(center=(max_width // 2, max_height // 2 +100))
recregresar = regresar.get_rect(bottomleft=(recfondo3.left, recfondo3.bottom-200))

import pygame
import AAAjuego

gato1 = pygame.image.load("programa-main/imagenes/gato1.png")
gato2 = pygame.image.load("programa-main/imagenes/gato2.png")

gato1 = pygame.transform.scale(gato1, (800, 800))
gato2 = pygame.transform.scale(gato2, (800, 800))


gato = gato1

recgato = gato.get_rect(center=(860, 640))



#funcion menu2
def menu2():
    
    running = True
    while running:

        current_time = pygame.time.get_ticks()
        if current_time % (3 * 1000) < (1 * 1000):
            pygame.display.update()
            gato = gato1
        elif current_time % (3 * 1000) < (2 * 1000):
            pygame.display.update()
            gato = gato2
        else:
            pygame.display.update()
            gato = gato1
            


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if recregresar.collidepoint(event.pos):
                    AAAjuego.juego()
                elif reclogincio.collidepoint(event.pos):
                    import logaritmos as logaritmos
                    pygame.display.update()
                    logaritmos.iniciar_cuestionario()

        
        # Blit images
        screen.blit(fondo3, recfondo3.topleft)
        screen.blit(logincio, reclogincio.topleft)
        screen.blit(regresar, recregresar.topleft)
        screen.blit(gato, recgato.topleft)
        pygame.display.update()

