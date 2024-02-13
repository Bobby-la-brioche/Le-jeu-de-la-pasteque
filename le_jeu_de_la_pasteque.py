#Les trucs pour que ça fonctionne
import pygame, sys
from pygame.locals import *
from entity import Entity
from mouse import Mouse
from scene import Scene
from constants import *
from bouton import Bouton_volume

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
Bouton_volume_on_ratio = 0.03
Bouton_volume_off_ratio = 0.03
Bouton_full_on_ratio= 0.03
Bouton_full_off_ratio= 0.03


# fond de la fenêtre
background = Entity(WINDOW_SIZE, WINDOW_BACKGROUND, 1, (0, 0), "contain",  hitbox=False)

# Boutons
Bouton_full_on = Entity(WINDOW_SIZE, FULLSCREEN_ON, Bouton_full_on_ratio)
Bouton_full_off = Entity(WINDOW_SIZE, FULLSCREEN_OFF, Bouton_full_off_ratio)
bouton_volume = Bouton_volume(WINDOW_SIZE, Bouton_volume_on_ratio, pos=(40,0))

# Souris
curseur = Mouse(WINDOW_SIZE, curseur_ratio)

mouse = pygame.mouse.get_pos()
scene = Scene()

scene.add_entity(background, bouton_volume, Bouton_full_on, Bouton_full_off, curseur)



# Musique
file = 'res/music_pasteque.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

t_volume=True
t_full= False




while True:
    # Affichage

    ecran.fill(FOND) 
    scene.draw(ecran)

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

        
        elif  event.type == MOUSEBUTTONUP and event.button==1:
            if bouton_volume.rect.collidepoint(mouse):
                bouton_volume.action_volume()             

        elif event.type == MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            curseur.updateState(WINDOW_SIZE, background.rect)
            curseur.pos = (mouse[0],mouse[1] if curseur.img_index==0 else background.pos[1]+30)



    ### 2 - Mise à jour des données ###
    scene.update() 

    ### Mise à jour pygame
    clock.tick(120)
    pygame.display.update() 