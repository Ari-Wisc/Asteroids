# import everything from a module
# into the current file
from constants import *
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill
        pygame.display.flip()



if __name__ == "__main__":
    main()