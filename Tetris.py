import os
import time
import random
import keyboard

# Dimensions of the board
WIDTH, HEIGHT = 10, 20

# Tetrimino shapes
SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
    'L': [[1, 0],
          [1, 0],
          [1, 1]],
    'J': [[0, 1],
          [0, 1],
          [1, 1]],
}

# Create an empty board
def create_board():
    return [[0] * WIDTH for _ in range(HEIGHT)]

# Draw the game board
def draw_board(board, score):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Score: {score}")
    for row in board:
        print(''.join('▌' if cell else ' ' for cell in row))
    print("=" * WIDTH)

# Check if a shape can be placed at a specific location
def can_place(shape, board, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell and (y + i >= HEIGHT or x + j < 0 or x + j >= WIDTH or board[y + i][x + j]):
                return False
    return True

# Place a shape on the board
def place_shape(shape, board, x, y):
    for i, row in enumerate(shape):
        for j, cell in enumerate(row):
            if cell:
                board[y + i][x + j] = cell

# Remove filled lines from the board
def clear_lines(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    cleared_lines = HEIGHT - len(new_board)
    return [[0] * WIDTH for _ in range(cleared_lines)] + new_board, cleared_lines

# Rotate a shape 90 degrees clockwise
def rotate_shape(shape):
    return [list(row) for row in zip(*shape[::-1])]

def main():
    board = create_board()
    current_shape = random.choice(list(SHAPES.values()))
    x, y = WIDTH // 2 - len(current_shape[0]) // 2, 0
    score = 0

    while True:
        # Draw the board and update the display
        draw_board(board, score)

        # Check for user input
        if keyboard.is_pressed('left') and can_place(current_shape, board, x - 1, y):
            x -= 1
        if keyboard.is_pressed('right') and can_place(current_shape, board, x + 1, y):
            x += 1
        if keyboard.is_pressed('down') and can_place(current_shape, board, x, y + 1):
            y += 1
        if keyboard.is_pressed('up'):
            rotated_shape = rotate_shape(current_shape)
            if can_place(rotated_shape, board, x, y):
                current_shape = rotated_shape

        # Move the shape down
        if not can_place(current_shape, board, x, y + 1):
            place_shape(current_shape, board, x, y)
            board, cleared_lines = clear_lines(board)
            score += cleared_lines
            current_shape = random.choice(list(SHAPES.values()))
            x, y = WIDTH // 2 - len(current_shape[0]) // 2, 0

            # Check for game over
            if not can_place(current_shape, board, x, y):
                draw_board(board, score)
                print("Game Over!")
                break
        else:
            y += 1

        # Slow down the game loop
        time.sleep(0.1)

if __name__ == "__main__":
    main()


