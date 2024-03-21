import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
CAR_WIDTH, CAR_HEIGHT = 50, 100
CAR_COLOR = (255, 0, 0)
CAR_SPEED = 5
TRACK_COLOR = (0, 255, 0)
TRACK_WIDTH = 20
FONT_SIZE = 32

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

def create_track(screen):
    track_surface = pygame.Surface((WIDTH, HEIGHT))
    track_surface.fill((0, 0, 0))
    pygame.draw.rect(track_surface, TRACK_COLOR, (0, 0, WIDTH, TRACK_WIDTH))
    pygame.draw.rect(track_surface, TRACK_COLOR, (0, HEIGHT - TRACK_WIDTH, WIDTH, TRACK_WIDTH))
    pygame.draw.rect(track_surface, TRACK_COLOR, (0, 0, TRACK_WIDTH, HEIGHT))
    pygame.draw.rect(track_surface, TRACK_COLOR, (WIDTH - TRACK_WIDTH, 0, TRACK_WIDTH, HEIGHT))
    screen.blit(track_surface, (0, 0))

car_rect = pygame.Rect(WIDTH / 2, HEIGHT - CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT)
previous_position = car_rect.x, car_rect.y

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_rect.x -= CAR_SPEED
    if keys[pygame.K_RIGHT]:
        car_rect.x += CAR_SPEED
    if keys[pygame.K_UP]:
        car_rect.y -= CAR_SPEED
    if keys[pygame.K_DOWN]:
        car_rect.y += CAR_SPEED

    if car_rect.x < 0:
        car_rect.x = 0
    if car_rect.x + CAR_WIDTH > WIDTH:
        car_rect.x = WIDTH - CAR_WIDTH
    if car_rect.y < 0:
        car_rect.y = 0
    if car_rect.y + CAR_HEIGHT > HEIGHT:
        car_rect.y = HEIGHT - CAR_HEIGHT

    distance = math.sqrt((car_rect.x - previous_position[0]) ** 2 + (car_rect.y - previous_position[1]) ** 2)
    speed_mps = distance / FPS
    speed_kmh = speed_mps * 3.6
    speed_text = font.render(f"Speed: {round(speed_kmh, 1)} km/h", True, (255, 255, 255))
    speed_rect = speed_text.get_rect(center=(WIDTH / 2, 50))

    screen.fill((0, 0, 0))
    create_track(screen)
    pygame.draw.rect(screen, CAR_COLOR, car_rect)
    screen.blit(speed_text, speed_rect)
    pygame.display.flip()

    previous_position = car_rect.x, car_rect.y

pygame.quit()
sys.exit()