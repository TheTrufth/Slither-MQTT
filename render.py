import hashlib
import pygame
from config import CELL_SIZE, COLORS, PLAYER_ID


def consistent_color(player_id):
    index = int(hashlib.md5(player_id.encode()).hexdigest(), 16) % len(COLORS)
    return COLORS[index]


def draw_snake(screen, snake, color):
    for segment in snake:
        pygame.draw.rect(
            screen,
            color,
            (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        )


def draw_all_players(screen, all_players):
    for pid, player in all_players.items():
        if pid == PLAYER_ID:
            continue
        color = consistent_color(pid)
        snake = player.get("snake", [])
        draw_snake(screen, snake, color)
