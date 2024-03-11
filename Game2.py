import pygame
import random
import sys
import openpyxl

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Create a Font object
font = pygame.font.Font('freesansbold.ttf', 32)

# Initialize the reaction list
reaction_list = []
CORRECT_COUNT = 0
# Game loop
repeat_count = 0
while repeat_count < 5:  # Repeat the game 5 times
    # Generate two random numbers
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Create a Text surface object for num1
    num1_text = font.render(str(num1), True, (255, 255, 255))
    num1_rect = num1_text.get_rect()
    num1_rect.center = (200, 200)

    # Create a Text surface object for num2
    num2_text = font.render(str(num2), True, (255, 255, 255))
    num2_rect = num2_text.get_rect()
    num2_rect.center = (600, 200)

    # Record the start time
    start_time = pygame.time.get_ticks()

    # Display the numbers on the screen
    screen.fill((0, 0, 0))
    screen.blit(num1_text, num1_rect)
    screen.blit(num2_text, num2_rect)
    pygame.display.update()

    # Get the sum of the numbers
    sum_of_numbers = num1 + num2

    # Input handling
    inputting = True
    player_input = ""
    while inputting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        if int(player_input) == sum_of_numbers:
                            # Calculate the duration and append it to the reaction list
                            end_time = pygame.time.get_ticks()
                            duration = end_time - start_time
                            reaction_list.append(duration)
                            CORRECT_COUNT += 1
                            print("Correct! Time taken:", duration, "ms")
                            
                        else:
                            print("Incorrect!")
                    except ValueError:
                        print("Invalid input!")
                    inputting = False
                    player_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    player_input = player_input[:-1]
                else:
                    if event.unicode.isnumeric():  # checking if the input is a number
                        player_input += event.unicode  # putting the input in the player_input var

    repeat_count += 1  # Increment the repeat count

pygame.quit()
print(reaction_list)

REACTION = sum(reaction_list) / len(reaction_list)
AGE = input("age : ")
SEXE = input("sexe : ")
RESULTAT_SCOLAIRE = input("resultat scolaire : ")

workbook = openpyxl.load_workbook('Data2.xlsx')

sheet = workbook.active

new_row = (REACTION, CORRECT_COUNT, AGE, SEXE, RESULTAT_SCOLAIRE)
sheet.append(new_row)

workbook.save('Data2.xlsx')
