import pygame
import subprocess
import sys

pygame.init()

largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Menu Snake")

fond = pygame.image.load("Menu_Snake.png")  
fond = pygame.transform.scale(fond, (largeur, hauteur))

blanc = (255, 255, 255)
noir = (0, 0, 0)

font = pygame.font.Font(None, 36)

def afficher_texte(texte, couleur, position):
    texte_surface = font.render(texte, True, couleur)
    texte_rect = texte_surface.get_rect(center=position)
    fenetre.blit(texte_surface, texte_rect)

while True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evenement.type == pygame.MOUSEBUTTONDOWN:
            if 300 < evenement.pos[0] < 500 and 250 < evenement.pos[1] < 350:
                subprocess.run(["python", "Snake\Snake.py"])

    fenetre.blit(fond, (0, 0))

    pygame.draw.rect(fenetre, blanc, (300, 250, 200, 100))
    afficher_texte("Jouer", noir, (400, 300))

    pygame.display.flip()
