import pygame
import sys
import numpy as np
import time
#
class Cell:
    def __init__(self,identity, state):
        self.identity = identity
        self.state = state
        self.neighbors = []
        self.signal = 0
        self.enabled = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def set_state(self, data):
        self.state = data
#
# Initialize Pygame
pygame.init()
#
# Set up the display
initial_size = (800, 600)
screen = pygame.display.set_mode(initial_size, pygame.RESIZABLE)
pygame.display.set_caption("Resizable Window Example")
#
# Define colors
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (100, 100, 100)
#
# Button colors corresponding to button indices
button_colors = [
    (255, 0, 0),   # RED - FIRING
    (0, 0, 255),   # BLUE - RESTING
    (255, 255, 0), # YELLOW - CONNECTOR
    (255, 165, 0), # ORANGE - POWER
    (100, 100, 100), # BLACK - EMPTY
    (0, 255, 0)    # GREEN - START
]
#
# Define button text
button_texts = ["FIRING", "RESTING", "CONNECTOR", "POWER", "EMPTY", "START"]
#
# Define state mapping for buttons
state_mapping = {
    "FIRING": 4,
    "RESTING": 3,
    "CONNECTOR": 2,
    "POWER": 1,
    "EMPTY": 0
}
#
# Grid and button settings
rows, cols = 16, 16
button_height = 40
num_buttons = len(button_texts)
cell_size = 30  # Default cell size
#
# Font setup
font = pygame.font.SysFont(None, 24)
#
# Function to draw the grid and color cells
def draw_grid(surface, rows, cols, button_rects, button_texts, current_color_cells):
    width, height = surface.get_size()
    cell_width = width // cols
    cell_height = (height - button_height) // rows
    #
    # Draw colored cells
    for coords, color in current_color_cells.items():
        x, y = coords
        rect = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
        pygame.draw.rect(surface, color, rect)
    #
    # Draw grid lines
    for x in range(cols + 1):
        pygame.draw.line(surface, WHITE, (x * cell_width, 0), (x * cell_width, height - button_height))
    for y in range(rows + 1):
        pygame.draw.line(surface, WHITE, (0, y * cell_height), (width, y * cell_height))
    #
    # Draw buttons with text and color
    for idx, rect in enumerate(button_rects):
        pygame.draw.rect(surface, button_colors[idx], rect)
        pygame.draw.rect(surface, WHITE, rect, 2)  # Draw border
        #
        # Draw button text
        if button_texts[idx]:
            text_surface = font.render(button_texts[idx], True, WHITE)
            text_rect = text_surface.get_rect(center=rect.center)
            surface.blit(text_surface, text_rect)
#
cell_array = np.empty((rows, cols), dtype=object)
#
#Fill array with cells with state 0
n = 0
for i in range(rows):
    for j in range(cols):
        cell_array[i, j] = Cell(n, 0)
        n += 1
#
#Fill neighbor array in cells
for i in range(rows):
    for j in range(cols):
        if i > 0:
            cell_array[i, j].add_neighbor(cell_array[i - 1, j])
        if j > 0:
            cell_array[i, j].add_neighbor(cell_array[i, j - 1])
        if j < len(cell_array) - 1:
            cell_array[i, j].add_neighbor(cell_array[i, j + 1])
        if i < len(cell_array) - 1:
            cell_array[i, j].add_neighbor(cell_array[i + 1, j])
#
building = True
running = False
current_color = button_colors[0]  # Default color is the first button color (RED)
current_color_map = {}
current_state = 4  # Default state corresponds to "FIRING"
#
#Main loop logic executed directly
while building:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #
            # Check if any button was clicked
            for idx, rect in enumerate(button_rects):
                if rect.collidepoint(mouse_x, mouse_y):
                    button_label = button_texts[idx]
                    if button_label == "START":
                        running = True
                        building = False # Print "START" if the START button is clicked
                    else:
                        current_color = button_colors[idx]  # Set the selected color
                        current_state = state_mapping[button_label]  # Set the current state (0-4)
            #
            # Determine the clicked cell if it's not on a button
            width, height = screen.get_size()
            cell_width = width // cols
            cell_height = (height - button_height) // rows
            if mouse_y < height - button_height:  # Ignore clicks on the button area
                clicked_cell = (mouse_x // cell_width, mouse_y // cell_height)
                current_color_map[clicked_cell] = current_color  # Handle cell coloring
                #
                # Print the cell's position and current state
                #
                cell_array[clicked_cell[1], clicked_cell[0]].set_state(current_state)
                #
                # Print Cell State, Testing

    # Fill the background
    screen.fill(BLACK)
    #
    # Draw the grid, colored cells, and buttons
    width, height = screen.get_size()
    button_width = width // (num_buttons + 1)  # Adjust width based on number of buttons
    button_x_start = (width - (button_width * num_buttons)) // 2
    button_y = height - button_height
    #
    button_rects = []
    for i in range(num_buttons):
        button_x = button_x_start + i * button_width
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        button_rects.append(button_rect)
    #
    draw_grid(screen, rows, cols, button_rects, button_texts, current_color_map)
    #
    # Update display
    pygame.display.flip()
#
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    for i in range(rows):
        for j in range(cols):
            if cell_array[i, j].state == 1:
                # Power Logic
            elif cell_array[i, j].state == 2:
                # Connecting Logic
            elif cell_array[i, j].state == 3:
                # Resting Logic
            elif cell_array[i, j].state == 4:
                # Firing Logic
    #
    # Print cell states while running is true
    for i in range(rows):
        for j in range(cols):
            print(cell_array[i, j].state, end=" ")
        print()  # Newline after each row
    print()  # Extra newline for spacing between iterations

    # Update display
    pygame.display.flip()
    time.sleep(1)
