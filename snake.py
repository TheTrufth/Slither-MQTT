from config import WINDOW_SIZE, CELL_SIZE


def move_snake(snake, direction):
    grid_size = WINDOW_SIZE // CELL_SIZE

    new_x = (snake[0][0] + direction[0]) % grid_size
    new_y = (snake[0][1] + direction[1]) % grid_size
    new_head = [new_x, new_y]

    snake.insert(0, new_head)
    snake.pop()
    return snake
