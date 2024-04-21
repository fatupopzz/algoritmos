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
pygame.display.set_caption('Juego')

# Load and scale images
directorio = "programa-main/imagenes"
fondo = scale_surface(pygame.image.load(f"{directorio}/fondo.png"), 1920, 1080)
titulo = scale_surface(pygame.image.load(f"{directorio}/titulo.png"), 1920, 1080)
jugar = scale_surface(pygame.image.load(f"{directorio}/inicio.png"),1920,1080)
salir = scale_surface(pygame.image.load(f"{directorio}/salida.png"), 800, 600)

salir = pygame.transform.scale(salir, (150, 150))
jugar = pygame.transform.scale(jugar, (150, 150))

# Get rects for images
recfondo = fondo.get_rect(center=(960, 540)) 
recbackground = titulo.get_rect(center=(960, 540))  
recjugar = jugar.get_rect(center=(960, 540))  
recsalir = salir.get_rect(center=(960, 740))  




def iniciar_juego():
    import AAAjuego as juego
    juego.juego()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if recjugar.collidepoint(event.pos):
                pygame.display.update()
                iniciar_juego()
            if recsalir.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    # Blit images
    screen.blit(fondo, recfondo.topleft)
    screen.blit(titulo, recbackground.topleft)
    screen.blit(jugar, recjugar.topleft)
    screen.blit(salir, recsalir.topleft)
    pygame.display.update()