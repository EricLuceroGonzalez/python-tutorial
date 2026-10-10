# pymunk-4.py
# https://www.youtube.com/watch?v=tLsi2DeUsak
#? (0) Importar librerias necesarias
import pygame
import pymunk
import pymunk.pygame_util
import math

#? (1) Iniciar todo
pygame.init()
ANCHO, ALTO = 600, 600
window = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("PYGAME: Simulación")


#? (2) 
def run(window, ancho, alto):
    run = True
    clock = pygame.time.Clock()
    fps = 60
    dt = 1/fps

    # ! CREAR ESPACIO
    space = pymunk.Space()
    space.gravity = (0, 981); # * Define la gravedad en x,y (y aumenta hacia abajo)

    # Crear bola con create_ball(), cuando se haga click
    ball = False
    # ball = create_ball(space, 30, 100)
    boundaries(space, ANCHO, ALTO)

    draw_options = pymunk.pygame_util.DrawOptions(window)

    while run:
        for event in pygame.event.get():  # Check events running
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                # ball.body.apply_impulse_at_local_point((5000, 500), (0,0))
                if not ball:
                    click_position = pygame.mouse.get_pos()
                    ball = create_ball(space, 30, 100, click_position)
            # ? Cuando las teclas son presionadas, aplicar fuerza (radio de la bola)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_LEFT:
                    ball.body.apply_impulse_at_world_point((-500, 0), (0,0))
                if event.key == pygame.K_RIGHT:
                    ball.body.apply_impulse_at_world_point((500, 0), (0,0))
                if event.key == pygame.K_UP:
                    ball.body.apply_impulse_at_world_point((0, 1000), (0,0))
                    # ball.body.apply_impulse_at_local_point((50000, 0), (0,0))

        draw(space, window, draw_options)
        space.step(dt) # Rapidez de la simulación
        clock.tick(fps)

    pygame.quit()


# ?(3) Draw funcion
def draw(space, window, draw_options):
    window.fill("white")
    space.debug_draw(draw_options)
    pygame.display.update()

# ?(4) Add object
def create_ball(space, radius, mass, click_position):
    body = pymunk.Body() # Create a rigid body
    body.position = click_position # Initial coordinates of the center of the body
    # shape = pymunk.Circle(body, radius)  # Característica del objeto
    shape = pymunk.Poly(body, [(0,0), (100,0), (0,100), (0,100)]) # ! Rectangulo
    # ! Definir atributos del objeto:
    shape.mass = mass
    shape.color = (255,100,0,255)
    shape.elasticity = 1.9
    shape.friction = 0.5
    space.add(body, shape)
    return shape

# ?(5) Static objects
def boundaries(space, width, height):
    rectangle=[
        [(width/2, height - 10), (width, 20)],
        [(width/2, 10), (width, 20)],
        [(10, height/2), (20, height)],
        [(width- 10, height/2), (20, height)],
    ]
    # rectangle = [
    #     [(0,600), (2*width, 10)]
    # ]
    for pos, size in rectangle:
        body = pymunk.Body(body_type=pymunk.Body.STATIC ) # Not move (not gravity)
        # body = pymunk.Body() #! Now move ( gravity)
        body.position = pos
        shape = pymunk.Poly.create_box(body, size) # http://www.pymunk.org/en/latest/pymunk.html#pymunk.Poly
        # shape = pymunk.Poly(body, [(0,0), (100,100), (0,100), (100,100)])
        # shape.mass = 100 #! Now move ( gravity)
        shape.elasticity = 0.4
        shape.friction = 0.5
        # body.angle = -0.5 # ! Rotar para un plano inclinado
        shape.color=(0,255,0,255)
        space.add(body, shape)

def calcular_distancia(P1,P2):
    return math.sqrt( (P2[1] - P1[1])**2 + (P2[0] - P1[0])**2)

def calcular_angulo(P1,P2):
    return math.atan2(P2[1]-P1[1], P2[0] - P1[0])

if __name__ == "__main__":
    run(window, ANCHO, ALTO)

