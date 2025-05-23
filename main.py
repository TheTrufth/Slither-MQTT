import pygame
import time
from config import *
from mqtt_client import start_mqtt, send_snake_state, players, send_disconnect
from snake import move_snake
from render import draw_snake, draw_all_players

pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption(f"Slither MQTT - {PLAYER_ID}")
clock = pygame.time.Clock()

snake = [[10, 10], [9, 10], [8, 10]]
direction = [1, 0]
running = True

last_publish_time = 0
PUBLISH_INTERVAL = 0.1  # seconds
start_mqtt()

last_time = time.time()  # Add this at the top of the game loop
while running:
    # Calculate delta_time (time elapsed since last frame)
    current_time = time.time()
    delta_time = current_time - last_time
    last_time = current_time
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != [1, 0]:
        direction = [-1, 0]
    elif keys[pygame.K_RIGHT] and direction != [-1, 0]:
        direction = [1, 0]
    elif keys[pygame.K_UP] and direction != [0, 1]:
        direction = [0, -1]
    elif keys[pygame.K_DOWN] and direction != [0, -1]:
        direction = [0, 1]
    elif keys[pygame.K_q]:
        running = False

    # Move the snake normally
    snake = move_snake(snake, direction, delta_time)

    # Publish the snake state
    if time.time() - last_publish_time >= PUBLISH_INTERVAL:
        send_snake_state(snake)
        last_publish_time = time.time()

    draw_snake(screen, snake, COLOR)
    draw_all_players(screen, players)

    pygame.display.flip()
    clock.tick(FPS)

send_disconnect()
pygame.quit()
