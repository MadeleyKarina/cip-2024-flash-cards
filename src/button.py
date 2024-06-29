import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font size for text
FONT_SIZE = 25

class Button:
    def __init__(self, menu_section_width, menu_section_rect, num_buttons) -> None:
        # Button properties (customize as needed)
        self.button_height = 50
        self.button_margin = 10
        self.button_colors = [(208, 224, 255), (200, 200, 255)]  # Default and hover colors
# rgb(208, 224, 255)
        self.num_buttons = num_buttons
        self.button_states = [False] * num_buttons

        # Calculate dynamic button width based on available space
        self.available_width = menu_section_width - (3 * self.button_margin)
        self.button_width = int(self.available_width)  # Ensure integer width

        self.menu_section_width = menu_section_width
        self.menu_section_rect = menu_section_rect

        self.font = pygame.font.SysFont(None, FONT_SIZE)

        self.positions = {}

    def get_button_rect(self, button_index):
        # Calculate button position based on index
        button_x = self.menu_section_rect.left + self.button_margin
        button_y = self.menu_section_rect.top + self.button_margin + (button_index * (self.button_height + self.button_margin))
        return pygame.Rect(button_x, button_y, self.button_width, self.button_height)

    def draw_buttons(self, screen, idx, text):
        #Track position and text
        self.positions[idx] = text
        # Draw the menu section
        button_rect = self.get_button_rect(idx)
        button_color = self.button_colors[1] if self.button_states[idx] else self.button_colors[0]  # Change color on hover/click
        pygame.draw.rect(screen, button_color, button_rect)
        
        # Text surfaces for question and answer (pre-render for efficiency)
        text_surface = self.font.render(text, True, BLACK)

        # Check if text width exceeds available space (accounting for margins)
        available_text_width = button_rect.width - self.button_margin * 2  # Adjust margin for text
        while text_surface.get_width() > available_text_width:
            # Iteratively shorten the text until it fits
            text = text[:-1]  # Remove the last character from the tag
            text_surface = self.font.render(text + '...', True, BLACK)  # Re-render with updated tag

        text_rect = text_surface.get_rect()
        x_center = button_rect.centerx - text_rect.width // 2
        y_center = button_rect.centery - text_rect.height // 2

        screen.blit(text_surface, (x_center, y_center))  # Adjust positioning for padding
        # Display text
        # screen.blit(text_surface, (button_rect.left + self.button_margin, button_rect.top + self.button_margin))  # Adjust positioning for padding
    
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

