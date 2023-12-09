#Les trucs pour que ça fonctionne
import pygame, sys, random
from pygame.locals import *


APP_TITLE = "Jeu de la pastèque"
APP_LOGO = "res/logo.png"

WINDOW_SIZE = (1236, 651)
WINDOW_BACKGROUND = "res/fond_boite_2.png"
SOURIS= "res/carotte2.png"
NUAGE= "res/nuage.png"

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

curseur_carotte     = pygame.image.load(SOURIS).convert_alpha()
curseur_nuage       = pygame.image.load(NUAGE).convert_alpha()
mouse               = pygame.mouse.get_pos()
curseur_carotte2    = curseur_carotte
curseur_nuage2      = curseur_nuage

taille_curseur_carotte=curseur_carotte.get_size()
taille_curseur_nuage=curseur_nuage.get_size()


#Couleurs

YELLOW  = (255, 255, 0)
GREEN   = (0, 255, 0)
BLANC   = (255,255,255)
ROUGE   = (255, 0, 0)
NOIR    = (0, 0, 0)
GRIS    = (155,155,155)
ROSE    = (180,50, 67)

fruits = []


#music
file = 'res/music_pasteque.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


#fonctions

def ratio(image):
    a=image.get_size()
    return(a[0]/a[1])

def taille(image):
    a=image.get_size()
    return(a[0],a[1])

while True:
    # actions utilisateurs (clavier, souris)
    # Les évènements regardés 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.VIDEORESIZE:
            WINDOW_SIZE=pygame.display.get_surface().get_size()
            background2 = pygame.transform.scale(background,WINDOW_SIZE)
            curseur_carotte2 = pygame.transform.scale(curseur_carotte,(taille(curseur_carotte)[0]*WINDOW_SIZE[0]/1000*ratio(curseur_carotte),taille(curseur_carotte)[1]*WINDOW_SIZE[1]/1000))
            

        # mise à jour des données 
    # pas encore fait 
 
    # affichage 
    ecran.fill(NOIR) 
    ecran.blit(background2, (0, 0)) 
     
    mouse = pygame.mouse.get_pos()



    if mouse[0]>=(7/24 *WINDOW_SIZE[0]) and mouse[0]<=(149/200 *WINDOW_SIZE[0]):
        pos=(mouse[0],(101/550)*WINDOW_SIZE[1])
        pygame.draw.line(ecran, ROSE, start_pos=pos, end_pos=(mouse[0],WINDOW_SIZE[1]), width=5)
        ecran.blit(curseur_nuage2,pos)
    else:
        ecran.blit(curseur_carotte2, mouse)


    clock.tick(120)
    pygame.display.update()
