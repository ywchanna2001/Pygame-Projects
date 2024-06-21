import pygame
import random
# from os.path import join
 
# Genaral setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

#importing an image
player_surf = pygame.image.load('images/player.png').convert_alpha()
star_surf = pygame.image.load('images/star.png').convert_alpha()
star_positions = [(random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)) for i in range(20)]


while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #draw the game
    #fill the window with the color
    display_surface.fill('darkgray')   #background
    
    #stars
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    #plane
    x += 0.1
    display_surface.blit(player_surf, (x, 150 ))
    pygame.display.update()


pygame.quit()