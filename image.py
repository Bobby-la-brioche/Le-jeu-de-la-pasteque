from pygame import Surface,transform
from pygame.locals import SRCALPHA



def fitImageScale(image: Surface, windowSize: tuple[int, int], ratio: float):
    w, h = image.get_size() # récupération de la taille de l'image
    imgRatio = w / h # calcul du ratio de l'image
    newW = int(windowSize[0] * ratio) # calcul de la nouvelle largeur
    newH = int(newW / imgRatio) # calcul de la nouvelle hauteur en fonction du ratio de l'image

    # pour des raisons de qualité d'images, on en refait une nouvelle au lieu de redimensionnée
    # celle d'origine qui a potentiellement déjà subit un redimensionnement et qui a donc perdu
    # de la qualité
    # Penser à initialiser la surface avec la transparence si l'image en possède
    img = Surface((w, h), flags=SRCALPHA)
    img.blit(image, (0, 0)) # copie de l'image d'origine dans la nouvelle
    img = transform.scale(img, (newW, newH)) # redimensionnement de l'image
    
    return img
