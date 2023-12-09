#Les trucs pour que ça fonctionne
import pygame, sys, random
from pygame.locals import *


APP_TITLE = "Jeu de la pastèque"
APP_LOGO = "res/logo.png"

WINDOW_SIZE = (1236, 651)
WINDOW_BACKGROUND = "res/fond_boite_2.png"
SOURIS= "res/carrotte2.png"


pygame.init()
pygame.display.set_caption(APP_TITLE)

# Créer l'icone AVANT la fenêtre
logo = pygame.image.load(APP_LOGO)
pygame.display.set_icon(logo)
pygame.mouse.set_visible(False)




#temps
clock = pygame.time.Clock()

# création de la fenêtre
ecran = pygame.display.set_mode(WINDOW_SIZE, RESIZABLE)
# fond de la fenêtre
background = pygame.image.load(WINDOW_BACKGROUND).convert()
background2 = background


#Souris

new_cursor = pygame.image.load(SOURIS)
mouse =    pygame.mouse.get_pos()

#Couleurs

YELLOW =   (255, 255, 0)
RED =      (255, 0, 0)
GREEN =    (0, 255, 0)
BLANC =    (255,255,255)
NOIR =     (0, 0, 0)

fruits = []


file = 'res/music_pasteque.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


while True:
    # actions utilisateurs (clavier, souris)
    # Les évènements regardés 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.VIDEORESIZE:
            background2 = pygame.transform.scale(background,pygame.display.get_surface().get_size())
 
    if mouse[0]<=(2/3 *WINDOW_SIZE[0]) and mouse[0]>=(1/3 *WINDOW_SIZE[0]):
        pygame.draw.line(NOIR, start_pos=mouse, end_pos=(mouse[0],WINDOW_SIZE[1]))
    




    # mise à jour des données
    # pas encore fait

    # affichage
    ecran.fill(NOIR)
    ecran.blit(background2, (0, 0))
    
    pos = pygame.mouse.get_pos()
    ecran.blit(new_cursor, pos) # t'as oublié game

    clock.tick(120)
    pygame.display.update()