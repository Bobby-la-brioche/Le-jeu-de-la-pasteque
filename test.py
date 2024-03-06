import pygame
import sys

class FallingRectangle:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed_y = 5  # Ajustez la vitesse de chute selon vos besoins

    def update(self):
        self.rect.y += self.speed_y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WINDOW_SIZE = (400, 400)

# Création de la fenêtre
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Rectangle tombant")

# Création du sol
sol_y = WINDOW_SIZE[1] - 50

# Création du rectangle tombant
rectangle = FallingRectangle(50, 0, 50, 50, (255, 0, 0))

# Boucle principale
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mise à jour du rectangle tombant
    rectangle.update()

    # Vérification si le rectangle touche le sol
    if rectangle.rect.bottom >= sol_y:
        print("Le rectangle a touché le sol!")
        rectangle.speed_y =0

    # Affichage
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), (0, sol_y, WINDOW_SIZE[0], 2))  # Dessin du sol
    rectangle.draw(screen)

    pygame.display.flip()

    # Limite de FPS
    clock.tick(60)
