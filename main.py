import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    stroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (stroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Asteroid_Field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        screen.fill("black") 
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        for roids in stroids:
            if roids.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(roids):
                    shot.kill()
                    roids.split()
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')


if __name__ == "__main__":
    main()
