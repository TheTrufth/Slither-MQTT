import time
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


def interpolate_snake(snake1, snake2, t):
    interp_snake = []
    for seg1, seg2 in zip(snake1, snake2):
        x = seg1[0] + (seg2[0] - seg1[0]) * t
        y = seg1[1] + (seg2[1] - seg1[1]) * t
        interp_snake.append([x, y])
    return interp_snake


def draw_all_players(screen, all_players):
    now = time.time()

    for pid, player in all_players.items():
        if pid == PLAYER_ID:
            continue

        history = player.get("history", [])
        color = consistent_color(pid)

        if len(history) < 2:
            # Not enough data yet
            draw_snake(screen, history[-1]["snake"], color) if history else None
            continue

        past = history[0]
        recent = history[1]

        # Time difference between updates
        dt = recent["time"] - past["time"]
        if dt == 0:
            t = 1.0
        else:
            t = min((now - recent["time"]) / dt + 1, 1.0)  # Blend forward

        interp = interpolate_snake(past["snake"], recent["snake"], t)
        draw_snake(screen, interp, color)
