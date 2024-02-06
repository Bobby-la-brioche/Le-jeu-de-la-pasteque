#Les trucs pour que ça fonctionne
import pygame, sys
from pygame.locals import *
from entity import Entity
from mouse import Mouse
from scene import Scene
from constants import *

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

curseur_ratio = 0.03
curseur_nuage_ratio = 0.05
Bouton_volume_on_ratio = 0.03
Bouton_volume_off_ratio = 0.03
Bouton_full_on_ratio= 0.03
Bouton_full_off_ratio= 0.03


# fond de la fenêtre
background = Entity(WINDOW_SIZE, WINDOW_BACKGROUND, 1, (0, 0), "contain",  hitbox=True)

# Boutons
Bouton_volume_on = Entity(WINDOW_SIZE, VOLUME_ON, Bouton_volume_on_ratio,)
Bouton_volume_off = Entity(WINDOW_SIZE, VOLUME_OFF, Bouton_volume_off_ratio)
Bouton_full_on = Entity(WINDOW_SIZE, FULLSCREEN_ON, Bouton_full_on_ratio)
Bouton_full_off = Entity(WINDOW_SIZE, FULLSCREEN_OFF, Bouton_full_off_ratio)


# Souris
curseur = Mouse(WINDOW_SIZE, curseur_ratio)

mouse = pygame.mouse.get_pos()
scene = Scene()

scene.add_entity(background, Bouton_volume_on, Bouton_volume_off, Bouton_full_on, Bouton_full_off, curseur)



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
            if Bouton_volume_on.img.get_rect().collidepoint(mouse):
                t_volume=not t_volume
                pygame.mixer.music.set_volume(1 if t_volume else 0)

        elif  event.type == MOUSEBUTTONUP and event.button==1:
            if Bouton_full_on.img.get_rect().collidepoint(mouse):
                t_full=not t_full
                pygame.display.toggle_fullscreen(1 if t_full else 0)

        elif event.type == MOUSEMOTION:
            mouse = pygame.mouse.get_pos()
            curseur.pos = (mouse[0], background.pos[1])
            curseur.updateState(WINDOW_SIZE, background.rect)

        elif  event.type == MOUSEBUTTONUP and event.button==1:
            if Bouton_volume_on.get_rect().collidepoint(mouse):
                t_volume=not t_volume
                pygame.mixer.music.set_volume(1 if t_volume else 0)


    ### 2 - Mise à jour des données ###
    scene.update()
      
    

    ### 2 - Mise à jour des données ###
 
    

    ### 3 - Affichage des éléments à l'écran ###

    # Si curseur sur la zone de dépôt
    '''if mouse[0] >= (7/24 * background.l_x) and mouse[0] <= (149/200 * background.l_x):
        # affichage ligne de dépôt
        pos=(mouse[0], (101/550) * WINDOW_SIZE[1])
        pygame.draw.line(ecran, ROSE, start_pos=pos, end_pos=(mouse[0], WINDOW_SIZE[1]), width=5)

        # affichage curseur nuage (centré)
        pos = (pos[0] - curseur_nuage.img.get_size()[0]/2, pos[1] - curseur_nuage.img.get_size()[1]/2)
        ecran.blit(curseur_nuage.img, pos)
    
    # si curseur en dehors de la zone de dépôt
    else:
        # affichage curseur carotte (top-left)
        ecran.blit(curseur_carotte.img, mouse)
'''

    ### Mise à jour pygame
    clock.tick(120)
    pygame.display.update() 