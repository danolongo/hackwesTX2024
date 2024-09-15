import pygame
import random

# Initialize Pygame
pygame.init()

# Set the number of rows and columns as variables
GRID_ROWS = 10  # You can change this value
GRID_COLS = 10  # You can change this value

# Set up display with a scalable window size
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600  # You can adjust this for different window sizes
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Interactive Scalable Matrix Grid")

# Colors for each value in the matrix
COLOR_MAP = {
    1: (255, 0, 0),   # Red for 1
    2: (0, 255, 0),   # Green for 2
    3: (0, 0, 255),   # Blue for 3
    4: (255, 255, 0)  # Yellow for 4
}

# Generate a random matrix with values between 1 and 4
def generate_matrix(rows, cols):
    return [[random.randint(1, 4) for _ in range(cols)] for _ in range(rows)]

# Generate the initial matrix based on GRID_ROWS and GRID_COLS
matrix = generate_matrix(GRID_ROWS, GRID_COLS)

def draw_grid():
    """Draws the grid based on the current screen size and matrix."""
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width // GRID_COLS
    cell_height = screen_height // GRID_ROWS

    # Loop through the matrix and draw corresponding colored squares
    for y in range(GRID_ROWS):
        for x in range(GRID_COLS):
            value = matrix[y][x]
            color = COLOR_MAP.get(value, (255, 255, 255))  # Default to white if value not found
            pygame.draw.rect(screen, color, (x * cell_width, y * cell_height, cell_width, cell_height))

def get_cell_from_mouse(pos):
    """Returns the grid cell (row, col) based on mouse position."""
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width // GRID_COLS
    cell_height = screen_height // GRID_ROWS

    x, y = pos
    col = x // cell_width
    row = y // cell_height
    return row, col

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Clear screen with white

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:  # Handle window resizing
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse click
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_cell_from_mouse(mouse_pos)

            # Toggle the color value on click (cycle between 1, 2, 3, and 4)
            if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
                matrix[row][col] = (matrix[row][col] % 4) + 1  # Change color by cycling values 1, 2, 3, 4

    # Draw the scalable grid
    draw_grid()

    pygame.display.flip()  # Update the display

pygame.quit()
