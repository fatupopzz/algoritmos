
import sys

#variables respuestas
def iniciar_cuestionario(pg, sys):

    import random
    # Configurar la pantalla
    screen = pg.display.set_mode((800, 600))
    pg.init()
    pg.display.set_caption('Logaritmos')
    # Configurar la fuente
    font = pg.font.Font(None, 36)

    #cuestionario de logaritmos 
    #preguntas
    preguntas = [
        { "pregunta": "¿Cuál es el logaritmo base 10 de 1000?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "¿Cuál es el logaritmo base 2 de 8?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "¿Cuál es el logaritmo base 5 de 125?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "¿Cuál es el logaritmo base 3 de 81?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        { "pregunta": "¿Cuál es el logaritmo base 4 de 64?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "2"
        },
        { "pregunta": "¿Cuál es el logaritmo base 10 de 100000?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        { "pregunta": "¿Cuál es el logaritmo base 2 de 16?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "¿Cuál es el logaritmo base 5 de 625?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "4"
        },
        { "pregunta": "¿Cuál es el logaritmo base 3 de 27?",
            "opciones": ["2", "3", "4", "5"],
            "respuesta": "3"
        },
        { "pregunta": "¿Cuál es el logaritmo base 4 de 256?",
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
        screen.blit(texto, (20, 20))

        # Renderizar las opciones
        opciones_rects = []
        for i, opcion in enumerate(pregunta["opciones"]):
            texto_opcion = font.render(f"{i + 1}. {opcion}", True, (255, 255, 255))
            opcion_rect = texto_opcion.get_rect(topleft=(20, 60 + i * 40))
            screen.blit(texto_opcion, opcion_rect.topleft)
            opciones_rects.append(opcion_rect)

            pg.draw.rect(screen, (255, 0, 0), opcion_rect, 2)  

        #Actualizar la pantalla
        pg.display.flip()
        
        #Usuario responde
        while True:
            opcion_seleccionada = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
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
                            opcion_seleccionada = True
                            break  # Break out of the inner loop to proceed to the next question
            if opcion_seleccionada:
                preguntas.remove(pregunta)
                screen.fill((0, 0, 0))

                # Renderizar el contador de respuestas correctas e incorrectas
                texto_correctas = font.render(f"Correctas: {correctas}", True, (255, 255, 255))
                texto_incorrectas = font.render(f"Incorrectas: {incorrectas}", True, (255, 255, 255))

                # Dibujar el contador en la pantalla
                screen.blit(texto_correctas, (20, 500))  # Ajusta las coordenadas según sea necesario
                screen.blit(texto_incorrectas, (20, 540))  # Ajusta las coordenadas según sea necesario

                pg.display.flip()
                break  # Break out of the inner loop to proceed to the next question



