import pygame
import sys
from collections import deque

# Initialize Pygame
pygame.init()

# Set up the display
cell_size = 30  # Size of each cell in pixels
width, height = 1500, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("100x100 Grid")

# Colors
WHITE = (255, 255, 255)
GREY = (128, 128, 128)  # Empty spaces
RED = (255, 0, 0)  # Firing neurons
BLUE = (0, 0, 255)  # Resting neurons
YELLOW = (255, 255, 0)  # Connector
DARK_GREEN = (0, 100, 0)  # Dark green for Start button

# Button definitions
button_width, button_height = 100, 50
button_colors = {
    'FIRING': RED,
    'RESTING': BLUE,
    'CONNECTOR': YELLOW,
    'EMPTY': GREY,
    'START': DARK_GREEN  # Start button will now be dark green
}
buttons = {
    'FIRING': pygame.Rect(50, height - button_height - 10, button_width, button_height),
    'RESTING': pygame.Rect(160, height - button_height - 10, button_width, button_height),
    'CONNECTOR': pygame.Rect(270, height - button_height - 10, button_width, button_height),
    'EMPTY': pygame.Rect(380, height - button_height - 10, button_width, button_height),
    'START': pygame.Rect(490, height - button_height - 10, button_width, button_height)
}

class Cell:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = GREY  # Default to empty space
        self.neighbors = []

    def set_color(self, color):
        self.color = color

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def get_cell_type(self):
        if self.color == RED:
            return "Firing Neuron"
        elif self.color == BLUE:
            return "Resting Neuron"
        elif self.color == YELLOW:
            return "Connector"
        else:
            return "Empty Space"

    def is_neuron(self):
        return self.color in [RED, BLUE]

    def is_firing(self):
        return self.color == RED

    def is_resting(self):
        return self.color == BLUE

    def is_connector(self):
        return self.color == YELLOW

    def draw(self, surface):
        rect = pygame.Rect(self.x * self.size, self.y * self.size, self.size, self.size)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, WHITE, rect, 1)

class Grid:
    def __init__(self, width, height, cell_size):
        self.cell_size = cell_size
        self.cells = {}
        self.create_grid(width, height)
    
    def create_grid(self, width, height):
        for x in range(0, width, self.cell_size):
            for y in range(0, height - button_height - 20, self.cell_size):
                cell_x = x // self.cell_size
                cell_y = y // self.cell_size
                self.cells[(cell_x, cell_y)] = Cell(cell_x, cell_y, self.cell_size)
        
        # Add neighbors (no diagonals)
        for (x, y), cell in self.cells.items():
            neighbors = [
                (x-1, y), (x+1, y),  # Left, Right
                (x, y-1), (x, y+1)   # Up, Down
            ]
            for nx, ny in neighbors:
                if (nx, ny) in self.cells:
                    cell.add_neighbor(self.cells[(nx, ny)])

    def draw(self, surface):
        for cell in self.cells.values():
            cell.draw(surface)
    
    def get_cell(self, x, y):
        return self.cells.get((x, y))

    def check_neutral_cells(self):
        """Prints the resting neurons connected to firing neurons via connectors."""
        resting_neurons = [cell for cell in self.cells.values() if cell.is_resting()]
        for neuron in resting_neurons:
            connected_firing_neurons = self.count_firing_connections(neuron)
            print(f"Resting Neuron at ({neuron.x}, {neuron.y}) is connected to {connected_firing_neurons} Firing Neuron(s)")

    def count_firing_connections(self, neuron):
        """Counts how many firing neurons are connected to the resting neuron via paths of connectors."""
        firing_connections = 0
        visited = set()
        found_firing_neurons = set()

        # Perform DFS from the resting neuron to find firing neurons via connectors
        def dfs(current_cell, prev_cell=None):
            visited.add(current_cell)

            for neighbor in current_cell.neighbors:
                if neighbor.is_connector() and neighbor not in visited:
                    dfs(neighbor, current_cell)
                elif neighbor.is_firing() and prev_cell.is_connector() and neighbor not in found_firing_neurons:
                    found_firing_neurons.add(neighbor)

        # Start the search from each connector adjacent to the resting neuron
        for neighbor in neuron.neighbors:
            if neighbor.is_connector() and neighbor not in visited:
                dfs(neighbor)

        return len(found_firing_neurons)

# Function to draw buttons with white borders
def draw_buttons():
    border_thickness = 1
    for name, rect in buttons.items():
        pygame.draw.rect(screen, button_colors[name], rect)
        border_rect = pygame.Rect(rect.x - border_thickness, rect.y - border_thickness, rect.width + 2 * border_thickness, rect.height + 2 * border_thickness)
        pygame.draw.rect(screen, WHITE, border_rect, border_thickness)
        font = pygame.font.SysFont(None, 24)
        text = font.render(name, True, WHITE)
        screen.blit(text, (rect.x + (button_width // 2 - text.get_width() // 2), rect.y + (button_height // 2 - text.get_height() // 2)))

# Main loop
running = True
current_color = GREY  # Default to empty spaces
grid = Grid(width, height, cell_size)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for name, rect in buttons.items():
                if rect.collidepoint(mouse_x, mouse_y):
                    if name == 'START':
                        grid.check_neutral_cells()  # Only print output when Start is pressed
                    else:
                        current_color = button_colors[name]

            if mouse_y < height - button_height - 20:
                clicked_cell = (mouse_x // cell_size, mouse_y // cell_size)
                cell = grid.get_cell(*clicked_cell)
                if cell:
                    cell.set_color(current_color)

    screen.fill(GREY)
    grid.draw(screen)
    draw_buttons()
    pygame.display.flip()

pygame.quit()
sys.exit()
