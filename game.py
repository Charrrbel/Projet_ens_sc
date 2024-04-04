import time
import pygame
import openpyxl
import random
import numpy as np

pygame.init()
t1 = time.time() 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

reaction_times = []
clock = pygame.time.Clock()
for i in range(5):
    screen.fill((255, 0, 0))
    pygame.display.update()
    t = random.randint(3,9)
    clock.tick(t/10)
    RUN = True
    screen.fill((0, 255, 0))
    START = time.time()
    while RUN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    END = time.time()
                    RUN = False                
        pygame.display.flip()
    
    reaction_time = (END - START)*1000
    if START - t1 < END - t1: 
        reaction_times.append(reaction_time)

pygame.quit()

REACTION = sum(reaction_times) / len(reaction_times)
print(REACTION)

reaction_times = np.array(reaction_times)
diffs = np.diff(reaction_times)
mean_diff = np.mean(diffs)
RATE = mean_diff/np.mean(reaction_times) * (-100)
print(RATE)
# VARIABLE ETUDIEE

AGE = input("age : ")
SEXE = input("sexe : ")
RESULTAT_SCOLAIRE = input("resultat scolaire : ")
CONSOMMATION_CAFFEINE = input("Consomme tu de la caffeine ?")
FATIGUE = input("Es-tu fatigué ?")
SOMMEIL = input("Combien d'heure de sommeil ?")
REVEIL = input("Combien d'heure depuis le reveil ?")
TEL = input("Combien d'heure de téléphone?")

# save to excel
workbook = openpyxl.load_workbook('Data1.xlsx')

sheet = workbook.active

new_row = (REACTION, AGE, SEXE, RESULTAT_SCOLAIRE, CONSOMMATION_CAFFEINE, FATIGUE, SOMMEIL, REVEIL, TEL)
sheet.append(new_row)

workbook.save('Data1.xlsx')
