# pymunk-4.py
# https://www.youtube.com/watch?v=tLsi2DeUsak
#? (0) Importar librerias necesarias
import pygame
import pymunk
import pymunk.pygame_util
import math

#? (1) Iniciar todo
pygame.init()
ANCHO, ALTO = 1000, 750
window = pygame.display.set_mode((ANCHO, ALTO))
# pygame.display.set_caption("PYGAME: Simulación")


#? (2) 
def run(window, ancho, alto):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps

    # ! CREAR ESPACIO
    space = pymunk.Space()
    space.gravity = (0, 981); # * Define la gravedad en x,y (y aumenta hacia abajo)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():  # Check events running
            if event.type == pygame.QUIT:
                run = False
                break
        draw(space, window, draw_options)
        space.step(dt) # Rapidez de la simulación
        clock.tick(fps)

        pygame.display.set_caption(str(pygame.time.get_ticks()/1000) + ' segundos')

    pygame.quit()


# ?(3) Draw funcion
def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

# Iniciar a correr el codigo con la variable especial __main__
if __name__ == "__main__":
    run(window, ANCHO, ALTO)