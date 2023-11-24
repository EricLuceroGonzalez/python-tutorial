import pymunk
import pygame
import os

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, -200)  # Set the gravity

#! Create a static ground segment
ground = pymunk.Segment(space.static_body, (0, 0), (800, 0), 0)
ground.friction = 1.0
ground.elasticity = 1
space.add(ground)

# Create a dynamic ball
ball_mass = 1
ball_radius = 30
ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
ball_body = pymunk.Body(ball_mass, ball_moment)
ball_body.position = (400, 300)
ball_shape = pymunk.Circle(ball_body, ball_radius)
ball_shape.elasticity = 0.5
space.add(ball_body, ball_shape)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = clock.tick(60) / 1000.0  # Convert to seconds

    space.step(dt)

    screen.fill((255, 255, 255))  # Clear the screen

    # Draw the Pymunk objects
    for shape in space.shapes:
        if isinstance(shape, pymunk.Segment):
            body = shape.body
            pv1 = body.position + shape.a.rotated(body.angle)
            pv2 = body.position + shape.b.rotated(body.angle)
            p1 = pv1.x, height - pv1.y
            p2 = pv2.x, height - pv2.y
            pygame.draw.line(screen, (0, 0, 0), p1, p2)
        elif isinstance(shape, pymunk.Circle):
            body = shape.body
            p = body.position + shape.offset.rotated(body.angle)
            p = p.x, height - p.y
            pygame.draw.circle(screen, (0, 0, 0), (int(p[0]), int(p[1])), int(shape.radius), 1)

    pygame.display.flip()  # Update the display

pygame.quit()