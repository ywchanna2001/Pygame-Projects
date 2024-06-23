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

#imports
player_surf = pygame.image.load('images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2 , WINDOW_HEIGHT /2))
player_dir = 1

meteor_surf = pygame.image.load('images/meteor.png').convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(WINDOW_WIDTH /2, WINDOW_HEIGHT /2))

laser_surf = pygame.image.load('images/laser.png').convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT - 20))

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
    
    display_surface.blit(meteor_surf,meteor_rect)
    display_surface.blit(laser_surf,laser_rect)
    #plane

    player_rect.x += player_dir * 0.4
    if(player_rect.right > WINDOW_WIDTH or player_rect.left < 0):
        player_dir *= -1 
    display_surface.blit(player_surf,player_rect )
    



    pygame.display.update()


pygame.quit()