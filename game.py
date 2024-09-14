import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
cell_size = 30  # Size of each cell in pixels
width, height = 1500, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("100x100 Grid")

# Colors
WHITE = (255, 255, 255)
BLACK = (100, 100, 100)
RED = (255, 0, 0)  # Color to highlight clicked cells

# Function to draw the grid
def draw_grid(highlighted_cells):
    for x in range(0, width, cell_size):
        for y in range(0, height, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            if (x // cell_size, y // cell_size) in highlighted_cells:
                pygame.draw.rect(screen, RED, rect)  # Fill the cell if it's clicked
            pygame.draw.rect(screen, WHITE, rect, 1)

# Main loop
running = True
highlighted_cells = []  # To store clicked cells
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Determine the clicked cell
            clicked_cell = (mouse_x // cell_size, mouse_y // cell_size)

            # Add the clicked cell to the highlighted list
            if clicked_cell not in highlighted_cells:
                highlighted_cells.append(clicked_cell)
            else:
                highlighted_cells.remove(clicked_cell)

    # Fill the background
    screen.fill(BLACK)

    # Draw the grid and highlight clicked cells
    draw_grid(highlighted_cells)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
