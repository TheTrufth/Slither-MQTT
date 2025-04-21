import pygame
from config import CELL_SIZE, COLORS, PLAYER_ID

def draw_snake(screen, snake, color):
    for segment in snake:
        pygame.draw.rect(screen, color, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_all_players(screen, all_players):
    for pid, segs in all_players.items():
        color = COLORS[hash(pid) % len(COLORS)]
        draw_snake(screen, segs, color)
