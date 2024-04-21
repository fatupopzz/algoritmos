import pygame as pg
import random
import sys


#variables respuestas
def iniciar_cuestionario():
    pg.init()
    font = pg.font.Font('programa-main/font/JELLYBELLY.TTF', 36)
    # Configurar la pantalla
    screen = pg.display.set_mode((1920, 1080))
    
    pg.display.set_caption('Logaritmos')
    # Configurar la fuente
    font = pg.font.Font('programa-main/font/JELLYBELLY.TTF', 36)


    # Cambiar el color del fondo a lila
    screen.fill((200, 0, 200))

    #cuestionario de logaritmos 
    #preguntas
    preguntas = [
        { "pregunta": "Cual es el logaritmo base 10 de 1000?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        { "pregunta": "Cual es el logaritmo base 2 de 8?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "Cual es el logaritmo base 5 de 125?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "Cual es el logaritmo base 3 de 81?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        { "pregunta": "Cual es el logaritmo base 4 de 64?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "Cual es el logaritmo base 10 de 100000?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "5"
        },
        { "pregunta": "Cual es el logaritmo base 2 de 16?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        { "pregunta": "Cual es el logaritmo base 5 de 625?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        { "pregunta": "Cual es el logaritmo base 3 de 27?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "Cual es el logaritmo base 4 de 256?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        }
    ]
    #Hacer el cuestionario
    correctas = 0
    incorrectas = 0
    while preguntas:
        pregunta = random.choice(preguntas)
        texto = font.render(pregunta["pregunta"], True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
        screen.blit(texto, texto_rect)

        # Renderizar las opciones
        opciones_rects = []
        for i, opcion in enumerate(pregunta["opciones"]):
            texto_opcion = font.render(f"{i + 1}. {opcion}", True, (255, 255, 255))
            opcion_rect = texto_opcion.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + i * 40))
            screen.blit(texto_opcion, opcion_rect)

            opciones_rects.append(opcion_rect)
            pg.draw.rect(screen, (255, 0, 0), opcion_rect, 2)

        # Renderizar el botón de regreso
        texto_regreso = font.render("Regresar al Menu", True, (255, 255, 255))
        regreso_rect = texto_regreso.get_rect(center=(screen.get_width() // 2, screen.get_height() - 170))
        screen.blit(texto_regreso, regreso_rect)
        pg.draw.rect(screen, (0, 255, 0), regreso_rect, 2)

        # Actualizar la pantalla
        pg.display.update()

        # Usuario responde
        running = True
        preguntas_respondidas = []
        while running:
            opcion_seleccionada = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return None
                elif event.type == pg.MOUSEBUTTONDOWN:
                    # Comprobar si el usuario ha hecho clic en alguna de las opciones
                    for i, opcion_rect in enumerate(opciones_rects):
                        if opcion_rect.collidepoint(event.pos):
                            # El usuario ha seleccionado esta opción
                            print(f"User selected option {i + 1}, correct answer is {pregunta['respuesta']}")
                            if pregunta["opciones"][i] == pregunta["respuesta"]:  # Comparar la opción seleccionada con la respuesta
                                correctas += 1
                                
                            else:
                                incorrectas += 1
                            running = False
                            opcion_seleccionada = True
                            break
                    # Comprobar si el usuario ha hecho clic en el botón de regreso
                    if regreso_rect.collidepoint(event.pos):
                        import menu2 as menu
                        screen.fill((0, 0, 0))
                        pg.display.update()
                        menu.menu2()
            if opcion_seleccionada:
                preguntas.remove(pregunta)
                screen.fill((200, 0, 200))
                
                # Renderizar el contador de respuestas correctas e incorrectas
                texto_correctas = font.render(f"Correctas: {correctas}", True, (255, 255, 255))
                texto_incorrectas = font.render(f"Incorrectas: {incorrectas}", True, (255, 255, 255))
                
                # Dibujar el contador en la pantalla
                texto_correctas_rect = texto_correctas.get_rect(center=(screen.get_width() // 2, screen.get_height() - 300))
                texto_incorrectas_rect = texto_incorrectas.get_rect(center=(screen.get_width() // 2, screen.get_height() - 250))
                screen.blit(texto_correctas, texto_correctas_rect)
                screen.blit(texto_incorrectas, texto_incorrectas_rect)


                # Actualizar la pantalla
                pg.display.update()
                pg.time.wait(200)  # Esperar 2 segundos antes de mostrar la siguiente pregunta
                break
iniciar_cuestionario()
