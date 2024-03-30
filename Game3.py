import pygame
import random
import openpyxl

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Create a Font object
font = pygame.font.SysFont('Segoe UI Symbol', 100)

# Game loop
game_count = 0
reaction_list = []
while game_count < 5:
    # Generate a random number
    num1 = random.randint(0, 15)  

    num_list = [u'\u2191',"up",u'\u2193',"down",u'\u2190', "left", u'\u2192', "right", u'\u2199', "down-left", u'\u2198', "down-right", u'\u2196', "up-left", u'\u2197', "up-right"]
    # Create a Text surface object for num1
    num1_text = font.render(num_list[num1], True, (255, 255, 255))
    num1_rect = num1_text.get_rect()
    num1_rect.center = (400, 300)

    # Display the numbers on the screen
    screen.fill((0, 0, 0))  # Fill the screen with black
    screen.blit(num1_text, num1_rect)
    pygame.display.update()

    # Start the timer
    start_time = pygame.time.get_ticks()
    # Input handling
    inputting = True
    while inputting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if num1 == 0 or num1 == 1:  # Up
                    if event.key == pygame.K_UP:
                        end_time = pygame.time.get_ticks()  # Calculate the time taken to answer
                        time_taken = end_time - start_time
                        reaction_list.append(time_taken)
                        inputting = False
                elif num1 == 2 or num1 == 3:  # Down
                    if event.key == pygame.K_DOWN:
                        end_time = pygame.time.get_ticks()  # Calculate the time taken to answer
                        time_taken = end_time - start_time
                        reaction_list.append(time_taken)
                        inputting = False
                elif num1 == 4 or num1 == 5:  # Left
                    if event.key == pygame.K_LEFT:
                        end_time = pygame.time.get_ticks()  # Calculate the time taken to answer
                        time_taken = end_time - start_time
                        reaction_list.append(time_taken)
                        inputting = False
                elif num1 == 6 or num1 == 7:  # Right
                    if event.key == pygame.K_RIGHT:
                        end_time = pygame.time.get_ticks()  # Calculate the time taken to answer
                        time_taken = end_time - start_time
                        reaction_list.append(time_taken)
                        inputting = False

        keys = pygame.key.get_pressed()
        if num1 == 8 or num1 == 9:  # Down-Left
            if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                end_time = pygame.time.get_ticks()
                time_taken = end_time - start_time
                reaction_list.append(time_taken)
                inputting = False
                pygame.display.update()
        elif num1 == 10 or num1 == 11:  # Down-Right
            if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                end_time = pygame.time.get_ticks()
                time_taken = end_time - start_time
                reaction_list.append(time_taken)
                inputting = False
                pygame.display.update()
        elif num1 == 12 or num1 == 13:  # Up-Left
            if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                end_time = pygame.time.get_ticks()
                time_taken = end_time - start_time
                reaction_list.append(time_taken)
                inputting = False
                pygame.display.update()
        elif num1 == 14 or num1 == 15:  # Up-Right
            if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                end_time = pygame.time.get_ticks()
                time_taken = end_time - start_time
                reaction_list.append(time_taken)
                inputting = False
                pygame.display.update()
    game_count += 1

pygame.quit()
print(reaction_list)

REACTION = sum(reaction_list) / len(reaction_list)
AGE = input("age : ")
SEXE = input("sexe : ")
RESULTAT_SCOLAIRE = input("resultat scolaire : ")
CONSOMMATION_CAFFEINE = input("Consomme tu de la caffeine ?")
FATIGUE = input("Es-tu fatigué ?")
SOMMEIL = input("Combien d'heure de sommeil ?")
REVEIL = input("Combien d'heure depuis le reveil ?")

workbook = openpyxl.load_workbook('Data3.xlsx')

sheet = workbook.active

new_row = (REACTION, AGE, SEXE, RESULTAT_SCOLAIRE, CONSOMMATION_CAFFEINE, FATIGUE, SOMMEIL, REVEIL)
sheet.append(new_row)

workbook.save('Data3.xlsx')
