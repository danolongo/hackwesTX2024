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
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
GREY = (192, 192, 192)  # Color for the Remove button

# Button definitions
button_width, button_height = 100, 50
button_colors = {'RED': RED, 'BLUE': BLUE, 'GREEN': GREEN, 'ORANGE': ORANGE, 'REMOVE': GREY}
buttons = {
    'RED': pygame.Rect(50, height - button_height - 10, button_width, button_height),
    'BLUE': pygame.Rect(160, height - button_height - 10, button_width, button_height),
    'GREEN': pygame.Rect(270, height - button_height - 10, button_width, button_height),
    'ORANGE': pygame.Rect(380, height - button_height - 10, button_width, button_height),
    'REMOVE': pygame.Rect(490, height - button_height - 10, button_width, button_height)  # Remove button
}

# Arrays to store the coordinates of colored cells
red_cells = []
blue_cells = []
green_cells = []
orange_cells = []

# Create a dictionary to map color names to their corresponding cell lists
color_cell_lists = {
    'RED': red_cells,
    'BLUE': blue_cells,
    'GREEN': green_cells,
    'ORANGE': orange_cells
}

# List of all color cell lists (excluding the current color list)
all_color_cell_lists = [red_cells, blue_cells, green_cells, orange_cells]

# Function to draw the grid and color cells
def draw_grid():
    for x in range(0, width, cell_size):
        for y in range(0, height - button_height - 20, cell_size):  # Limit grid to not overlap buttons
            rect = pygame.Rect(x, y, cell_size, cell_size)
            cell_coords = (x // cell_size, y // cell_size)

            # Check which array the cell belongs to and draw the appropriate color
            if cell_coords in red_cells:
                pygame.draw.rect(screen, RED, rect)
            elif cell_coords in blue_cells:
                pygame.draw.rect(screen, BLUE, rect)
            elif cell_coords in green_cells:
                pygame.draw.rect(screen, GREEN, rect)
            elif cell_coords in orange_cells:
                pygame.draw.rect(screen, ORANGE, rect)
            pygame.draw.rect(screen, WHITE, rect, 1)

# Function to draw buttons
def draw_buttons():
    for name, rect in buttons.items():
        pygame.draw.rect(screen, button_colors[name], rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render(name, True, WHITE)
        screen.blit(text, (rect.x + (button_width // 2 - text.get_width() // 2), rect.y + (button_height // 2 - text.get_height() // 2)))

# Main loop
running = True
current_color = 'RED'  # Default color

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if any button was clicked
            for name, rect in buttons.items():
                if rect.collidepoint(mouse_x, mouse_y):
                    if name == 'REMOVE':
                        # Clear all colored cells
                        for cells in all_color_cell_lists:
                            cells.clear()
                    else:
                        current_color = name  # Set the selected color

            # Determine the clicked cell if it's not on a button
            if mouse_y < height - button_height - 20:  # Ignore clicks on the button area
                clicked_cell = (mouse_x // cell_size, mouse_y // cell_size)

                # Remove clicked_cell from all lists except the one corresponding to current_color
                for cells in all_color_cell_lists:
                    if cells is not color_cell_lists[current_color] and clicked_cell in cells:
                        cells.remove(clicked_cell)

                # Add the clicked cell to the list corresponding to current_color if not already present
                if clicked_cell not in color_cell_lists[current_color]:
                    color_cell_lists[current_color].append(clicked_cell)

    # Fill the background
    screen.fill(BLACK)

    # Draw the grid and color the cells
    draw_grid()

    # Draw buttons
    draw_buttons()
    print(blue_cells , ",", green_cells)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
