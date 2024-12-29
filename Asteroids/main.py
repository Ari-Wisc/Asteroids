# import everything from a module
# into the current file
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
def main():
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    dt=0
    clock =pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers=(updatable)
    asteroidField=AsteroidField()
    
    while(True): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for thing in updatable:
            thing.update(dt)
        for asteroid in asteroids:
            if(player.colision(asteroid)):             
                print("Game over!")
                return
            for shot in shots:
                if(shot.colision(asteroid)):
                    shot.kill()
                    asteroid.split()

        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)  
        # player.draw(screen)
        pygame.display.flip() 
        dt=(clock.tick(60))/1000.0




if __name__ == "__main__":
    main()