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
    1: (255, 0, 0),  # Red for 1
    2: (0, 255, 0),  # Green for 2
    3: (0, 0, 255),  # Blue for 3
    4: (255, 255, 0)  # Yellow for 4
}

# Button settings
button_rect = pygame.Rect(10, 10, 100, 50)
button_color = (0, 255, 0)  # Green
button_text_color = (0, 0, 0)  # Black
button_text_font = pygame.font.Font(None, 36)


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


def draw_button():
    """Draw the start button on the screen."""
    pygame.draw.rect(screen, button_color, button_rect)
    text_surface = button_text_font.render('Start', True, button_text_color)
    screen.blit(text_surface, (button_rect.x + 10, button_rect.y + 10))


# Main loop
running = True
is_running = False  # Control the grid behavior
while running:
    screen.fill((255, 255, 255))  # Clear screen with white

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:  # Handle window resizing
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse click
            mouse_pos = pygame.mouse.get_pos()
            if button_rect.collidepoint(mouse_pos):
                # Toggle the running state
                is_running = not is_running
                button_color = (255, 0, 0) if is_running else (0, 255, 0)  # Red if running, green otherwise
            else:
                row, col = get_cell_from_mouse(mouse_pos)
                # Toggle the color value on click (cycle between 1, 2, 3, and 4)
                if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
                    matrix[row][col] = (matrix[row][col] % 4) + 1  # Change color by cycling values 1, 2, 3, 4

    # Draw the scalable grid
    draw_grid()

    # Draw the start button
    draw_button()

    pygame.display.flip()  # Update the display

pygame.quit()

