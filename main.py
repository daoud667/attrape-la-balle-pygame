import pygame
import random

pygame.init()

LARGEUR, HAUTEUR = 800, 600
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Attrape la balle !")

raquette_largeur, raquette_hauteur = 100, 10
raquette_x = LARGEUR // 2 - raquette_largeur // 2
raquette_y = HAUTEUR - 50
vitesse_raquette = 10

balle_x = random.randint(20, LARGEUR - 20)
balle_y = 50
balle_rayon = 15
balle_vitesse_x = 4
balle_vitesse_y = 4

score = 0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)
    ecran.fill(BLANC)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and raquette_x > 0:
        raquette_x -= vitesse_raquette
    if touches[pygame.K_RIGHT] and raquette_x < LARGEUR - raquette_largeur:
        raquette_x += vitesse_raquette

    balle_x += balle_vitesse_x
    balle_y += balle_vitesse_y

    if balle_x - balle_rayon <= 0 or balle_x + balle_rayon >= LARGEUR:
        balle_vitesse_x *= -1
    if balle_y - balle_rayon <= 0:
        balle_vitesse_y *= -1

    if (raquette_y <= balle_y + balle_rayon <= raquette_y + raquette_hauteur) and (raquette_x <= balle_x <= raquette_x + raquette_largeur):
        balle_vitesse_y *= -1
        score += 1

    if balle_y > HAUTEUR:
        score = 0
        balle_x = random.randint(20, LARGEUR - 20)
        balle_y = 50

    pygame.draw.rect(ecran, NOIR, (raquette_x, raquette_y, raquette_largeur, raquette_hauteur))
    pygame.draw.circle(ecran, ROUGE, (balle_x, balle_y), balle_rayon)
    texte = font.render(f"Score : {score}", True, NOIR)
    ecran.blit(texte, (10, 10))

    pygame.display.flip()

pygame.quit()
