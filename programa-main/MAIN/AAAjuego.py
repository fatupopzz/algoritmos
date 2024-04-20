import pygame as pg
import sys
from pygame.locals import *
from pygame.locals import QUIT
import pygame as pg
from pygame.locals import *
from pygame.locals import QUIT



max_width = 1920
max_height = 1080


pg.init()
screen = pg.display.set_mode((1920, 1080))
pg.display.set_caption('Menu')

def scale_surface(surface, width, height):
    width, height = surface.get_size()
    scale = min(max_width / width, max_height / height)
    return pg.transform.scale(surface, (int(width * scale), int(height * scale)))



def juego():
    directorio = "programa-main/imagenes"
    #imagenes
    fondo2 = scale_surface(pg.image.load(directorio + "/fondo2.png"), max_width, max_height)
    inicio = scale_surface(pg.image.load(directorio + "/jugar.png"), max_width // 8, max_height // 4).convert_alpha()
    salir = scale_surface(pg.image.load(directorio + "/salir.png"), max_width // 8, max_height // 4).convert_alpha()

    #personaje
    orb1 = scale_surface(pg.image.load(directorio + "/orbfeliz.png"), max_width // 2, max_height // 2).convert_alpha()
    orb2 = scale_surface(pg.image.load(directorio + "/orbnormal.png"), max_width // 2, max_height // 2).convert_alpha()
    orb3 = scale_surface(pg.image.load(directorio + "/orbtriste.png"), max_width // 2, max_height // 2).convert_alpha()
    #estadisticas
    stats1 = scale_surface(pg.image.load(directorio + "/stats1.png"), max_width // 2, max_height // 2).convert_alpha()
    stats2 = scale_surface(pg.image.load(directorio + "/stats2.png"), max_width // 2, max_height // 2).convert_alpha()
    stats3 = scale_surface(pg.image.load(directorio + "/stats3.png"), max_width // 2, max_height // 2).convert_alpha()
    recfondo = fondo2.get_rect(center=(960, 540))

    #inicio de orb
    orb = orb1
    stats = stats1

    # Definir el tamaño de los rectángulos
    ancho_boton = 200  # Cambia esto al ancho deseado
    alto_boton = 200  # Cambia esto al alto deseado

    #reemplazar por el tamaño de la imagen
    imagenjugar = pg.image.load(directorio + "/jugar.png")
    imagensalir = pg.image.load(directorio + "/salir.png")
    imagensalir = pg.transform.scale(imagensalir, (70, 70))

    # Calcular las posiciones de los rectángulos
    x_jugar = recfondo.centerx - ancho_boton // 2 -100
    y_jugar = recfondo.centery - alto_boton // 2 + 350
    x_salir = recfondo.centerx + 70
    y_salir = recfondo.centery - alto_boton // 2 + 350
    #rect imagenes
    recorb =  orb.get_rect(center=(max_width // 2, max_height // 2))
    recstats = stats.get_rect(center=(max_width // 2, max_height // 2))
    recjugar = imagenjugar.get_rect(center=(x_jugar + 300 // 2, x_jugar + 300 // 2))
    recsalir = imagensalir.get_rect(center=(x_salir + ancho_boton // 2, y_salir + alto_boton // 2))
   

    while True:
        tiempo = pg.time.get_ticks()  # Get the current time in milliseconds
        screen.blit(fondo2, recfondo.topleft)
        screen.blit(orb, recorb.topleft)
        screen.blit(stats, recstats.topleft)
        screen.blit(imagenjugar, recjugar.topleft)  # Dibujar la imagen de jugar
        screen.blit(imagensalir, recsalir.topleft)  # Dibujar la imagen de salir

        pg.display.update()

        # Cambiar orb cada 3 segundos
        if tiempo % (3 * 1000) < (1 * 1000):
            orb = orb1
            stats = stats1
        elif tiempo % (3 * 1000) < (2 * 1000):
            orb = orb2
            stats = stats2
        else:
            orb = orb3
            stats = stats3


        #boton de salida
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if recjugar.collidepoint(event.pos):
                    import menu2 as menu
                    pg.display.update()
                    menu.menu2()
                if recsalir.collidepoint(event.pos):
                    pg.quit()
                    sys.exit()
                pg.display.update()

       
    
       
    
