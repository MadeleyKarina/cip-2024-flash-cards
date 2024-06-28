import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font size for text
FONT_SIZE = 30

class Button:
    def __init__(self, menu_section_width, menu_section_rect, num_buttons) -> None:
         # Button properties (customize as needed)
        self.button_width = 100
        self.button_height = 50
        self.button_margin = 10
        self.button_colors = [(200, 200, 255), (150, 150, 255)]  # Default and hover colors

        self.num_buttons = num_buttons
        self.button_states = [False] * num_buttons

        self.menu_section_width = menu_section_width
        self.menu_section_rect = menu_section_rect

        self.font = pygame.font.SysFont(None, FONT_SIZE)

        self.positions = {}

    def get_button_rect(self, button_index):
        # Calculate button position based on index
        button_x = self.menu_section_rect.left + self.button_margin
        button_y = self.menu_section_rect.top + self.button_margin + (button_index * (self.button_height + self.button_margin))
        return pygame.Rect(button_x, button_y, self.button_width, self.button_height)

    def draw_buttons(self, screen, idx, tag):
        #Track position and tag
        self.positions[idx] = tag
        # Draw the menu section
        button_rect = self.get_button_rect(idx)
        button_color = self.button_colors[1] if self.button_states[idx] else self.button_colors[0]  # Change color on hover/click
        pygame.draw.rect(screen, button_color, button_rect)
        
        # Text surfaces for question and answer (pre-render for efficiency)
        tag_surface = self.font.render(tag, True, BLACK)

        # Display tag text
        screen.blit(tag_surface, (button_rect.left + 10, button_rect.top + 10))  # Adjust positioning for padding
    
    def handle_button_click(self, mouse_pos):
        # Check click within button rect for each button
        for i in range(self.num_buttons):
            button_rect = self.get_button_rect(i)
            if button_rect.collidepoint(mouse_pos):
                # Toggle button state and clear flashcards (if any)
                self.button_states = [False] * self.num_buttons
                self.button_states[i] = not self.button_states[i]

                return self.positions[i]
    def get_clicked_tag(self):
        # Return the tag associated with the clicked button (if any)
        for i, button_state in enumerate(self.button_states):
            if button_state:
                return self.positions.get(i)  # Use get to handle potential missing key
        return None  # Return None if no button is clicked

