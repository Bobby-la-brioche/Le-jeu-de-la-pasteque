#Les trucs pour que ça fonctionne
import pygame, sys
from pygame.locals import *
from entity import Entity
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

# Retourne une image redimensionnée pour qu'elle prenne la taille de la fenêtre
# Il faut donner l'image d'origine, sinon, si on redimensionne une image déjà redimensionnée,
# on risque de perdre en qualité :
# originale -> petite -> grande = perte de qualité car grande copie les pixels de petite
def fitImageScale(image: pygame.Surface, windowSize: tuple[int, int], ratio: float):
    w, h = image.get_size() # récupération de la taille de l'image
    imgRatio = w / h # calcul du ratio de l'image
    newW = int(windowSize[0] * ratio) # calcul de la nouvelle largeur
    newH = int(newW / imgRatio) # calcul de la nouvelle hauteur en fonction du ratio de l'image

    # pour des raisons de qualité d'images, on en refait une nouvelle au lieu de redimensionnée
    # celle d'origine qui a potentiellement déjà subit un redimensionnement et qui a donc perdu
    # de la qualité
    # Penser à initialiser la surface avec la transparence si l'image en possède
    img = pygame.Surface((w, h), flags=SRCALPHA)
    img.blit(image, (0, 0)) # copie de l'image d'origine dans la nouvelle
    img = pygame.transform.scale(img, (newW, newH)) # redimensionnement de l'image
    
    return img



APP_TITLE = "Jeu de la pastèque"
APP_LOGO = "res/logo.png"

WINDOW_SIZE = (1236, 651)
WINDOW_BACKGROUND = "res/fond_boite_2.png"
SOURIS= "res/carotte2.png"
NUAGE= "res/nuage.png"
VOLUME_ON= "res/volume-on.png"
VOLUME_OFF= "res/volume-off.png"
FULLSCREEN_ON= "res/full-screen-on.png"
FULLSCREEN_OFF= "res/full-screen-off.png"

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

<<<<<<< HEAD
# % par rapport à la largeur de la fenêtre

curseur_carotte_ratio = 0.03
curseur_nuage_ratio = 0.05
Bouton_volume_on_ratio = 0.03
Bouton_volume_off_ratio = 0.03
Bouton_full_on_ratio= 0.03
Bouton_full_off_ratio= 0.03


# fond de la fenêtre
background = Entity(WINDOW_SIZE, WINDOW_BACKGROUND, 0.05, (0, 0), "contain")

# Boutons
Bouton_volume_on = Entity(WINDOW_SIZE, VOLUME_ON, Bouton_volume_on_ratio)
Bouton_volume_off = Entity(WINDOW_SIZE, VOLUME_OFF, Bouton_volume_off_ratio)
Bouton_full_on = Entity(WINDOW_SIZE, FULLSCREEN_ON, Bouton_full_on_ratio)
Bouton_full_off = Entity(WINDOW_SIZE, FULLSCREEN_OFF, Bouton_full_off_ratio)


# Souris
curseur_carotte     = Entity(WINDOW_SIZE, SOURIS, curseur_carotte_ratio)
curseur_nuage       = Entity(WINDOW_SIZE, NUAGE, curseur_nuage_ratio)

=======

# fond de la fenêtre
background_original = pygame.image.load(WINDOW_BACKGROUND).convert()
background = background_original.copy()

#Boutons
Bouton_volume_on_og = pygame.image.load(VOLUME_ON).convert_alpha()
Bouton_volume_off_og = pygame.image.load(VOLUME_OFF).convert_alpha()
Bouton_full_on_og = pygame.image.load(FULLSCREEN_ON).convert_alpha()
Bouton_full_off_og = pygame.image.load(FULLSCREEN_OFF).convert_alpha()


#Souris
curseur_carotte_originale     = pygame.image.load(SOURIS).convert_alpha()
curseur_nuage_originale       = pygame.image.load(NUAGE).convert_alpha()

curseur_carotte = curseur_carotte_originale.copy()
curseur_nuage = curseur_nuage_originale.copy()

>>>>>>> 098f8d3f335ba21715dcf849a59a845b7c3eac92
mouse = pygame.mouse.get_pos()

# % par rapport à la largeur de la fenêtre
curseur_carotte_ratio = 0.03
curseur_nuage_ratio = 0.05
Bouton_volume_on_ratio = 0.03
Bouton_volume_off_ratio = 0.03
Bouton_full_on_ratio= 0.03
Bouton_full_off_ratio= 0.2

<<<<<<< HEAD



scene = Scene()

scene.add(background, curseur_carotte, curseur_nuage, Bouton_volume_on, Bouton_volume_off, Bouton_full_on, Bouton_full_off)



=======
# Fit une première fois car l'évènement "pygame.VIDEORESIZE" n'est pas appelé au lancement du programme
# Et il faut bien faire cette opération une première fois

curseur_carotte = fitImageScale(curseur_carotte_originale, WINDOW_SIZE, curseur_carotte_ratio)
curseur_nuage = fitImageScale(curseur_nuage_originale, WINDOW_SIZE, curseur_nuage_ratio)
Bouton_volume_on = fitImageScale(Bouton_volume_on_og, WINDOW_SIZE, Bouton_volume_on_ratio)
Bouton_volume_off = fitImageScale(Bouton_volume_off_og, WINDOW_SIZE, Bouton_volume_off_ratio)
Bouton_full_on = fitImageScale(Bouton_full_on_og, WINDOW_SIZE, Bouton_full_on_ratio)
Bouton_full_off = fitImageScale(Bouton_full_off_og, WINDOW_SIZE, Bouton_full_off_ratio)

# Un peu particulier pour le background :
# On veut être sûr que l'image de fond soit toujours visible en ENTIER
# Donc il faut savoir quel est le limitant entre la largeur et la hauteur
# Si bgRatio > 1 : la largeur est le limitant
# Sinon c'est la hauteur

bgRatio = getImageRatio(background_original)
background = fitImageScale(background_original, WINDOW_SIZE, min(1, bgRatio))

# Couleurs
YELLOW  = (255, 255, 0)
GREEN   = (0, 255, 0)
BLANC   = (255,255,255)
ROUGE   = (255, 0, 0)
NOIR    = (0, 0, 0)
GRIS    = (155,155,155)
ROSE    = (180,50, 67)


>>>>>>> 098f8d3f335ba21715dcf849a59a845b7c3eac92
# Musique
file = 'res/music_pasteque.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

t_volume=True
t_full= False

while True:
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
<<<<<<< HEAD
            WINDOW_SIZE = pygame.display.get_surface().get_size()

            scene.fitActors(WINDOW_SIZE)

        
        elif  event.type == MOUSEBUTTONUP and event.button==1:
            if Bouton_volume_on.img.get_rect().collidepoint(pygame.mouse.get_pos()):
                t_volume=not t_volume
                pygame.mixer.music.set_volume(1 if t_volume else 0)

        elif  event.type == MOUSEBUTTONUP and event.button==1:
            if Bouton_full_on.img.get_rect().collidepoint(pygame.mouse.get_pos()):
                t_full=not t_full
                pygame.display.toggle_fullscreen(1 if t_full else 0)


    ### 2 - Mise à jour des données ###
    scene.update()


    curseur_carotte.pos = mouse
    curseur_nuage.pos = mouse

 
    # Affichage 
    ecran.fill(NOIR) # /?\ Pourquoi ne pas mettre le fond de la même couleur que la couleur unie de background ?
    ecran.blit(background.img, (0, 0)) # /?\ Idée : mettre le fond à la position en bas de la fenêtre, au centre au lieu d'en haut à gauche
    
    
    if not t_full:
        ecran.blit(Bouton_full_off.img, (50,10))
    else:
        ecran.blit(Bouton_full_on.img, (50,10))

    if not t_volume:    
        ecran.blit(Bouton_volume_off.img, (10,10))
    else:
        ecran.blit(Bouton_volume_on.img, (10,10))
=======
            WINDOW_SIZE=pygame.display.get_surface().get_size()
            # Mise à jour de la taille du fond
            bgRatio = getImageRatio(background_original)
            background = fitImageScale(background_original, WINDOW_SIZE, min(1, bgRatio))
            # Mise à jour de la taille des curseurs
            curseur_carotte = fitImageScale(curseur_carotte_originale, WINDOW_SIZE, curseur_carotte_ratio)
            curseur_nuage = fitImageScale(curseur_nuage_originale, WINDOW_SIZE, curseur_nuage_ratio)
            #mise à jour de la taille des boutons
            Bouton_volume_on = fitImageScale(Bouton_volume_on_og, WINDOW_SIZE, Bouton_volume_on_ratio)
            Bouton_volume_off = fitImageScale(Bouton_volume_off_og, WINDOW_SIZE, Bouton_volume_off_ratio)
            Bouton_full_off = fitImageScale(Bouton_full_off_og, WINDOW_SIZE, Bouton_full_off_ratio)
            Bouton_full_on = fitImageScale(Bouton_full_on_og, WINDOW_SIZE, Bouton_full_on_ratio)

        
        elif  event.type == MOUSEBUTTONUP and event.button==1:
            if Bouton_volume_on.get_rect().collidepoint(mouse):
                t_volume=not t_volume
                pygame.mixer.music.set_volume(1 if t_volume else 0)

            elif Bouton_full_off.get_rect().collidepoint(mouse):
                t_full=not t_full
                pygame.display.toggle_fullscreen(1 if t_full else 0)
                print("jambon")

    ### 2 - Mise à jour des données ###
 
    # Affichage 
    ecran.fill(NOIR) # /?\ Pourquoi ne pas mettre le fond de la même couleur que la couleur unie de background ?
    ecran.blit(background, (0, 0)) # /?\ Idée : mettre le fond à la position en bas de la fenêtre, au centre au lieu d'en haut à gauche
    
    
    if not t_full:
        ecran.blit(Bouton_full_on, (1/20*WINDOW_SIZE[0],10))
    else:
        ecran.blit(Bouton_full_on, (1/20*WINDOW_SIZE[0],10))

    if not t_volume:    
        ecran.blit(Bouton_volume_off, (10,10))
    else:
        ecran.blit(Bouton_volume_on, (10,10))

    
    
>>>>>>> 098f8d3f335ba21715dcf849a59a845b7c3eac92

    mouse = pygame.mouse.get_pos()


    ### 3 - Affichage des éléments à l'écran ###

    # Si curseur sur la zone de dépôt
    if mouse[0] >= (7/24 * WINDOW_SIZE[0]) and mouse[0] <= (149/200 * WINDOW_SIZE[0]):
        # affichage ligne de dépôt
        pos=(mouse[0], (101/550) * WINDOW_SIZE[1])
        pygame.draw.line(ecran, ROSE, start_pos=pos, end_pos=(mouse[0], WINDOW_SIZE[1]), width=5)

        # affichage curseur nuage (centré)
<<<<<<< HEAD
        pos = (pos[0] - curseur_nuage.img.get_size()[0]/2, pos[1] - curseur_nuage.img.get_size()[1]/2)
        ecran.blit(curseur_nuage.img, pos)
=======
        pos = (pos[0] - curseur_nuage.get_size()[0]/2, pos[1] - curseur_nuage.get_size()[1]/2)
        ecran.blit(curseur_nuage, pos)
>>>>>>> 098f8d3f335ba21715dcf849a59a845b7c3eac92
    
    # si curseur en dehors de la zone de dépôt
    else:
        # affichage curseur carotte (top-left)
<<<<<<< HEAD
        ecran.blit(curseur_carotte.img, mouse)

    scene.draw(ecran)
=======
        ecran.blit(curseur_carotte, mouse)
>>>>>>> 098f8d3f335ba21715dcf849a59a845b7c3eac92

    ### Mise à jour pygame
    clock.tick(120)
    pygame.display.update() 