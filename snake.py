from config import WINDOW_SIZE, CELL_SIZE, GRID_SIZE


def check_wall_collision(snake):
    head = snake[0]
    if head[0] < 0 or head[0] >= GRID_SIZE or head[1] < 0 or head[1] >= GRID_SIZE:
        return True
    return False


def check_self_collision(snake):
    head = snake[0]
    for segment in snake[1:]:
        if head == segment:
            return True
    return False


SNAKE_SPEED = 10  # 10 cells per second (adjust this for desired speed)


def move_snake(snake, direction, delta_time):
    head = snake[0]

    # Move the head by SNAKE_SPEED * delta_time (in grid cells)
    new_head = [
        head[0] + direction[0] * SNAKE_SPEED * delta_time,
        head[1] + direction[1] * SNAKE_SPEED * delta_time,
    ]

    # Wrap horizontally and vertically using modulo arithmetic
    new_head[0] %= GRID_SIZE
    new_head[1] %= GRID_SIZE

    # Add the new head to the snake, remove the last tail segment to maintain length
    new_snake = [new_head] + snake[:-1]

    return new_snake
