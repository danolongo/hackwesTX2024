import MiscFun
import pygame

# Initialize Pygame
pygame.init()

# Set the number of rows and columns as variables
rows, cols = (17, 17)

# Set up display with a scalable window size
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600  # You can adjust this for different window sizes
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Brain of Life")

# Colors for each value in the matrix
COLOR_MAP = {
    0: (165, 165, 165), # Grey # dead
    1: (255, 165, 0), # Orange # power
    2: (0, 255, 255),  # Cyan # transistors
    3: (75, 0, 75), # Dark Purple #Resting Neurons
    4: (255, 75, 255) # Purple #Firing Neurons
}

cell_array = []

MiscFun.fill_cell_array(rows, cols, cell_array)
MiscFun.fill_cell_array_neighbors(rows, cols, cell_array)

button_rect = pygame.Rect(10, 10, 100, 50)
button_color = (255, 255, 255)  # Green
button_text_color = (0, 0, 0)  # Black
button_text_font = pygame.font.Font(None, 36)
button_width, button_height = 100, 50

def draw_grid():
    """Draws the grid based on the current screen size and matrix."""
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width // cols
    cell_height = screen_height // rows

    # Loop through the matrix and draw corresponding colored squares
    for y in range(rows):
        for x in range(cols):
            value = cell_array[y][x].state
            color = COLOR_MAP.get(value)  # Default to white if value not found
            pygame.draw.rect(screen, color, (x * cell_width, y * cell_height, cell_width, cell_height))

def get_cell_from_mouse(pos):
    """Returns the grid cell (row, col) based on mouse position."""
    screen_width, screen_height = screen.get_size()
    cell_width = screen_width // cols
    cell_height = screen_height // rows

    x, y = pos
    col = x // cell_width
    row = y // cell_height
    return row, col

def draw_button():
    screen_width, screen_height = screen.get_size()
    button_rect = pygame.Rect(screen_width - button_width - 10, screen_height - button_width - 10, button_width, button_width)
    pygame.draw.rect(screen, button_color, button_rect)
    text_surface = button_text_font.render('Start', True, button_text_color)
    screen.blit(text_surface, (button_rect.x + 10, button_rect.y + 10))

# Main loop
running = True
is_running = True
while running:
    #screen.fill((255, 255, 255))  # Clear screen with white
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:  # Handle window resizing
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Handle mouse click
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_cell_from_mouse(mouse_pos)

            if button_rect.collidepoint(mouse_pos):
                if is_running == True:
                    is_running = False
                else:
                    is_running = True
            # Toggle the color value on click (cycle between 1, 2, 3, and 4)
            if is_running == True:
                if 0 <= row < rows and 0 <= col < cols:
                    if cell_array[row][col].get_state() < 4:
                        cell_array[row][col].set_state(cell_array[row][col].get_state() + 1)
                    else:
                        cell_array[row][col].set_state(0)

    draw_grid()

    #draw_button()
    #print(is_running)
    pygame.display.flip()  # Update the display

pygame.quit()