import pygame
import textwrap

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)  # Color for unflipped card frame
BLUE = (0, 0, 255)  # Color for flipped card frame

# Font size for text
FONT_SIZE = 23

class FlashCard:
    def __init__(self, question, answer, x, y, start_y, width, height):
        self.question = question

        self.answer = answer
        self.x = x
        self.y = y
        self.start_y = start_y

        self.card_width = width
        self.card_height = height

        if (
            pygame.font is not None
        ):  # Check if pygame.font is available (indirect init check)
            self.font = pygame.font.SysFont(None, FONT_SIZE)
        else:
            print("Warning: Pygame might not be initialized. Font creation might fail.")

        # Calculate maximum text width that fits within the card with margins
        self.text_width_limit = width - 30  # Adjust margin for text
        # Calculate maximum number of lines that fit within card height
        self.max_lines = int(height / self.font.get_linesize()) - 2  # Adjust for padding

        # Pre-render full question and answer surfaces (for reference)
        self.full_question_surface = self.font.render(self.question, True, BLACK)
        self.full_answer_surface = self.font.render(self.answer, True, BLACK)

        # Create line-broken text surfaces initially (updated in draw method)
        self.question_surface = self.break_lines(self.question)
        self.answer_surface = self.break_lines(self.answer)

        self.is_flipped = False  # Track if the card is flipped

    def break_lines(self, text):
        # Wrap text with a character limit per line to ensure width fit
        char_width = self.font.size(" ")[0]  # Get character width
        max_chars_per_line = int(self.text_width_limit / char_width) - 1  # Adjust for potential word breaks
        wrapped_lines = textwrap.wrap(text, width=max_chars_per_line, max_lines=self.max_lines)
       
        surfaces = []

        current_line = ""
        for line in wrapped_lines:
            # Iteratively shorten the line until it fits within width limit
            current_line += line
            current_exceed = " "
            while self.font.size(current_line)[0] > self.text_width_limit:  # Adjust for potential word cut-off
                current_line = current_line.split()
                current_exceed = " " + current_line[-1] + current_exceed
                current_line = " ".join(current_line[:-1])  # Remove the last character
            
            surfaces.append(self.font.render(current_line.strip(), True, BLACK))
            current_line = current_exceed
        
        while current_line != "":
            current_exceed = ""
            while self.font.size(current_line)[0] > self.text_width_limit:  # Adjust for potential word cut-off
                current_line = current_line.split()
                current_exceed = " " + current_line[-1] + current_exceed
                current_line = " ".join(current_line[:-1]) # Remove the last character
            
            surfaces.append(self.font.render(current_line.strip(),True, BLACK))
            current_line = current_exceed
        
        return surfaces

    def draw(self, screen):
         # Draw a rectangle for the card with border
        border_size = 2  # Adjust border thickness

        # Draw a rectangle for the card
        pygame.draw.rect(screen, WHITE, (self.x, self.y + self.start_y, self.card_width, self.card_height))

        # Display question or answer based on flipped state
        x = self.x + 10
        y = self.y + self.start_y + 10
        line_height = self.font.get_linesize()  # Get line height for spacing
         # Draw inner rectangle with different color based on flipped state
        inner_rect = pygame.Rect(self.x, self.y + self.start_y, self.card_width, self.card_height)
       
        if self.is_flipped:
            pygame.draw.rect(screen, GREY, inner_rect, border_size)  # Draw black outer border
            for text_surface in self.answer_surface:
                text_rect = text_surface.get_rect()
                x_center = (self.x + self.card_width // 2) - text_rect.width // 2
                screen.blit(text_surface, (x_center, y))  # Adjust positioning for padding
                y += line_height
        else:
            pygame.draw.rect(screen, BLUE, inner_rect, border_size)  # Draw black outer border
            for text_surface in self.question_surface:
                text_rect = text_surface.get_rect()
                x_center = (self.x + self.card_width // 2) - text_rect.width // 2
                screen.blit(text_surface, (x_center, y))
                y += line_height

    def handle_click(self, pos):
        # Check if click is within the card's boundaries
        if (
            self.x < pos[0] < self.x + self.card_width
            and (self.y + self.start_y) < pos[1] < (self.y + self.start_y) + self.card_height
        ):
            self.is_flipped = not self.is_flipped  # Flip the card state
