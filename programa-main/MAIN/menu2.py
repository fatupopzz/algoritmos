import pygame 
import sys
from pygame.locals import *
from pygame.locals import QUIT

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
recfondo = fondo3.get_rect(center=(960, 530))
reclogincio = logincio.get_rect(center=(max_width // 2, max_height // 2))
recregresar = regresar.get_rect(bottomleft=(recfondo.left, recfondo.bottom-100))

#funcion menu2
def menu2():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if reclogincio.collidepoint(event.pos):
                        import random
                        import logaritmos as logaritmos
                        logaritmos.iniciar_cuestionario(pygame, sys)
                    if recregresar.collidepoint(event.pos):
                        import AAAjuego as juego
                        juego.juego()
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            # Blit images
            screen.blit(fondo3, recfondo.topleft)
            screen.blit(logincio, reclogincio.topleft)
            screen.blit(regresar, recregresar.topleft)
            pygame.display.update()

