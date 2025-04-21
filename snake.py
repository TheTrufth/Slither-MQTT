def move_snake(snake, direction):
    new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    snake.insert(0, new_head)
    snake.pop()  # No food yet
    return snake
