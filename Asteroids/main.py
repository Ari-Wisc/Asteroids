# import everything from a module
# into the current file
from constants import *
from player import Player
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
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable.add(player)
    drawable.add(player)
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for thing in updatable:
            thing.update(dt)
        screen.fill((0, 0, 0))

        for thing in drawable:
            thing.draw(screen)  
        # player.draw(screen)
        pygame.display.flip() 
        dt=(clock.tick(60))/1000.0




if __name__ == "__main__":
    main()