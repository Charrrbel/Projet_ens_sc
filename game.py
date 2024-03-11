import time
import pygame
import openpyxl

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill((255, 0, 0))
pygame.display.update()
clock = pygame.time.Clock()
clock.tick(0.4)
START = time.time()
RUN = True
while RUN:
    screen.fill((0, 255, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            END = time.time()
            RUN = False
    pygame.display.flip()
pygame.quit()

REACTION = (END - START)*1000
print(REACTION)

AGE = input("age : ")
SEXE = input("sexe : ")
RESULTAT_SCOLAIRE = input("resultat scolaire : ")

workbook = openpyxl.load_workbook('Data1.xlsx')

# Get the active sheet
sheet = workbook.active

new_row = (REACTION, AGE, SEXE, RESULTAT_SCOLAIRE)
sheet.append(new_row)

workbook.save('Data1.xlsx')
