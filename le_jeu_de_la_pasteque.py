#Les trucs pour que ça fonctionne
import pygame, sys
from pygame.locals import *
from entity import Entity
from mouse import Mouse
from scene import Scene
from constants import *
from boutons import Bouton_volume, Bouton_screen
from fruits import Fruit
from line import Ligne

# /!\ Toute fonction appelée doit être déclarée avant ses appels
# Généralement on met les fonctions en haut du fichier avant le code principal

# /i\ Note : dans une fonction, l'écriture (param: type) -> type de retour
# est facultative, mais permet de mieux comprendre le code
# et aussi, si on utilise un IDE comme VSC, d'avoir les propositions
# lorsqu'on écrit les variables car il sait son type donc ses fonctions possibles

# /!\ Toute fonction appelée doit être déclarée avant ses appels
# Généralement on met les fonctions en haut du fichier avant le code principal

# /i\ Note : dans une fonction, l'écriture (param: type) -> type de retour
# est facultative, mais permet de mieux comprendre le code
# et aussi, si on utilise un IDE comme VSC, d'avoir les propositions
# lorsqu'on écrit les variables car il sait son type donc ses fonctions possibles

# Retourne le ratio de l'image donnée en paramètre
# ratio = largeur / hauteur
def getImageRatio(image: pygame.Surface) -> float:
    w, h = image.get_size() # renvoie un tuple (largeur, hauteur) que l'on décompose
    return w / h


# Initialisation de pygame
pygame.init()
pygame.display.set_caption(APP_TITLE)

# Créer l'icone AVANT la fenêtre
logo = pygame.image.load(APP_LOGO)
pygame.display.set_icon(logo)
pygame.mouse.set_visible(False)

# création de la fenêtre
ecran = pygame.display.set_mode(WINDOW_SIZE, RESIZABLE)

# temps
clock = pygame.time.Clock()

# % par rapport à la largeur de la fenêtre

curseur_ratio = 0.045
Bouton_volume_ratio = 0.03
Bouton_screen_ratio= 0.03


# fond de la fenêtre
background = Entity(WINDOW_SIZE, WINDOW_BACKGROUND, 1, (0, 0), "contain",  hitbox=False)
sol= Ligne((0, WINDOW_SIZE[1]),(WINDOW_SIZE),(0,0,255))

# Boutons
bouton_screen= Bouton_screen(WINDOW_SIZE, Bouton_screen_ratio)
bouton_volume = Bouton_volume(WINDOW_SIZE, Bouton_volume_ratio, pos=(40,0))

# Souris
curseur = Mouse(WINDOW_SIZE, curseur_ratio)
mouse = pygame.mouse.get_pos()

#Fruits:

orange=Fruit(WINDOW_SIZE, ORANGE, 0.05, ecran, (200,200))

#Scene:

scene = Scene()

scene.add_entity(background, bouton_volume, bouton_screen, curseur, sol, orange)



# Musique
file = 'res/music_pasteque.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


while True:
    # Affichage

    ecran.fill(FOND) 
    scene.draw(ecran, WINDOW_SIZE)

    ### 1 - Gestion des évènements ###
    
    # Actions utilisateurs (clavier, souris)
    for event in pygame.event.get():

        # appuie sur la croix de la titlebar
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # Redimensionnement fenêtre
        elif event.type == pygame.VIDEORESIZE:
            # Mise à jour de la constante de la taille de la fenêtre
            WINDOW_SIZE = pygame.display.get_surface().get_size()
            scene.fit_image(WINDOW_SIZE)
            sol.start_point=(0, WINDOW_SIZE[1])
            sol.end_point= WINDOW_SIZE

        # Relever le bouton de la souris
        elif  event.type == MOUSEBUTTONUP and event.button==1:
            if bouton_volume.rect.collidepoint(mouse):
                bouton_volume.action_volume(WINDOW_SIZE)
            if bouton_screen.rect.collidepoint(mouse):
                bouton_screen.action_screen(WINDOW_SIZE)
        
        #appuyer sur la souris
        elif event.type == MOUSEBUTTONDOWN and curseur.img_index ==1 and orange.accroche:
            Fruit.tomber(orange)
        
        elif event.type == MOUSEBUTTONDOWN and curseur.img_index ==1 and not orange.accroche:
            Fruit.statique(orange)
            Fruit.ramener_souris(orange, (curseur.pos[0], curseur.pos[1]+curseur.rect.height+1))
                             
        # Bouger la souris
        elif event.type == MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            curseur.updateState(WINDOW_SIZE, background.rect, orange.hitbox)
            curseur.pos = (mouse[0],mouse[1] if curseur.img_index==0 else background.pos[1]+30)

            if curseur.img_index==1 and orange.accroche:
                orange.pos = (curseur.pos[0], curseur.pos[1]+curseur.rect.height+1)
            elif not curseur.img_index==1 and orange.accroche:
                orange.pos=(background.rect.w/2, background.pos[1]-orange.rect.h-10)
    
    ### 2 - Mise à jour des données ###
    scene.update() 

    ### Mise à jour pygame
    clock.tick(120)
    pygame.display.update() 