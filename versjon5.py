import pygame
import sys
import random
from pygame import mixer
from button import Button  

bredde = 1024
høyde = 1024

pygame.init()
SCREEN = pygame.display.set_mode((1024, 1024))  

# Bakgrunnsmusikk
mixer.music.load('snowfall.mp3')
mixer.music.play(-1)  # Spiller musikken i en loop

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def play():
    global bil_x, bil_y, b_pos, o_pos, snowflakes
    
    BG = pygame.image.load('vei2.jpg')
    overlapp = pygame.image.load('vei2.jpg')

    b_pos = 0
    o_pos = 1024
    hastighet = 10

    # Bilen
    bil = pygame.image.load('bil2premium.png')
    bil_x = 200
    bil_y = 500

    # Snowflakes
    snowflakes = []
    snowflake_size = 30
    snowflake_speed = 9

    # Create initial snowflakes
    num_snowflakes = 200
    for _ in range(num_snowflakes):
        snowflake = pygame.image.load('snowflake.png')  # Load snowflake image
        snowflake = pygame.transform.scale(snowflake, (snowflake_size, snowflake_size))  # Resize snowflake
        snowflake_x = random.randint(0, bredde)
        snowflake_y = random.randint(-høyde, 0)
        snowflakes.append((snowflake, snowflake_x, snowflake_y))

    clock = pygame.time.Clock()

    def move_snowflakes():
        for i, (snowflake, snowflake_x, snowflake_y) in enumerate(snowflakes):
            snowflake_y += snowflake_speed
            if snowflake_y > høyde:
                snowflake_y = -høyde
                snowflake_x = random.randint(0, bredde)
            # Check for collision with ground
            if snowflake_y + snowflake_size > høyde:
                snowflake_y = random.randint(-høyde, 0)
                snowflake_x = random.randint(0, bredde)
            snowflakes[i] = (snowflake, snowflake_x, snowflake_y)

    SCREEN.blit(BG, (0, 0))  # Display game background
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            bil_x -= 5  # Adjust car position to the left
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            bil_x += 5  # Adjust car position to the right
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            hastighet = 20 #Akselererer bilen
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            hastighet = 5 #Sakker ned bilen
        if keys[pygame.K_SPACE]:
            hastighet = 10 #Setter bilen til startfarten
        if keys[pygame.K_1]:
            hastighet = 40 #GTR-mode


        if b_pos >= høyde:
            b_pos = -høyde
        if o_pos >= høyde:
            o_pos = -høyde

        b_pos += hastighet
        o_pos += hastighet

        move_snowflakes()

        SCREEN.blit(BG, (0, b_pos))
        SCREEN.blit(overlapp, (0, o_pos))

        SCREEN.blit(bil, (bil_x, bil_y))

        for snowflake, snowflake_x, snowflake_y in snowflakes:
            SCREEN.blit(snowflake, (snowflake_x, snowflake_y))

        pygame.display.update()
        clock.tick(60)

def credits():
    while True:
        CREDITS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        CREDITS_TEXT = get_font(25).render("By Orlando Olaf Thalberg, 3STD", True, "Black")
        CREDITS_RECT = CREDITS_TEXT.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 4))
        SCREEN.blit(CREDITS_TEXT, CREDITS_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.fill((0, 0, 0))  # Display black screen

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render("Silent Ride", True, "#b68f40")  # Changed to Silent Ride
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 5))  # Adjusted vertical position

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 3 ), #SCREEN.get_height() // 3, får den lenger opp
                            text_input="PLAY", font=get_font(60), base_color="#d7fcd4", hovering_color="White")
        CREDITS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 3+150), #Høyere SCREEN-verdi, lenger ned
                            text_input="CREDITS", font=get_font(60), base_color="#d7fcd4", hovering_color="White")  # Changed to CREDITS
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(SCREEN.get_width() // 2, SCREEN.get_height() // 3+300), 
                            text_input="QUIT", font=get_font(60), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, CREDITS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if CREDITS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    credits()  # Changed to credits()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# Initial entry point to the program
main_menu()
