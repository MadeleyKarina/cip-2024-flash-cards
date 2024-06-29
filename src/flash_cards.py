import pygame
import textwrap

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font size for text
FONT_SIZE = 23


class FlashCard:
    def __init__(self, question, answer, x, y, width, height):
        self.question = question

        self.answer = answer
        self.x = x
        self.y = y

        self.card_width = width
        self.card_height = height

        if (
            pygame.font is not None
        ):  # Check if pygame.font is available (indirect init check)
            self.font = pygame.font.SysFont(None, FONT_SIZE)
        else:
            print("Warning: Pygame might not be initialized. Font creation might fail.")

        # Calculate maximum text width that fits within the card with margins
        self.text_width_limit = width - 20  # Adjust margin for text
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
        # Wrap text using textwrap, ensuring lines fit within width limit
        # wrapped_text = textwrap.wrap(text, width=self.text_width_limit // self.font.size(" ")[0])
        # wrapped_text = textwrap.wrap(text, width=self.text_width_limit // self.font.size(" ")[0], max_lines=self.max_lines)
        
         # Wrap text with a character limit per line to ensure width fit
        char_width = self.font.size(" ")[0]  # Get character width
        max_chars_per_line = int(self.text_width_limit / char_width) - 1  # Adjust for potential word breaks
        wrapped_lines = textwrap.wrap(text, width=max_chars_per_line, max_lines=self.max_lines)
        # wrapped_lines = textwrap.wrap(text, width=self.text_width_limit // self.font.size(" ")[0], max_lines=self.max_lines)
       
        surfaces = []
        current_exceed = ""
        current_line = ""
        for line in wrapped_lines:
            # Iteratively shorten the line until it fits within width limit
            current_line += line
            current_exceed = ""
            while self.font.size(current_line)[0] > self.text_width_limit - 10:  # Adjust for potential word cut-off
                current_exceed = current_line[-1] + current_exceed
                current_line = current_line[:-1]  # Remove the last character
            surfaces.append(self.font.render(current_line, True, BLACK))
            current_line = current_exceed
        
        if current_line != "":
            surfaces.append(self.font.render(current_line,True, BLACK))
        
        return surfaces
    
        # for line in wrapped_text:
        #     surfaces.append(self.font.render(line, True, BLACK))
        # return surfaces

    def draw(self, screen, start_y):
        # Draw a rectangle for the card
        pygame.draw.rect(screen, WHITE, (self.x, self.y + start_y, self.card_width, self.card_height))

        # Display question or answer based on flipped state
        x = self.x + 10
        y = self.y + start_y + 10
        line_height = self.font.get_linesize()  # Get line height for spacing

        if self.is_flipped:
            for surface in self.answer_surface:
                screen.blit(surface, (x, y))  # Adjust positioning for padding
                y += line_height
        else:
            for surface in self.question_surface:
                screen.blit(surface, (x, y))
                y += line_height
            # screen.blit(self.question_surface[0], (x, y))

    def handle_click(self, pos):
        # Check if click is within the card's boundaries
        if (
            self.x < pos[0] < self.x + self.card_width
            and self.y < pos[1] < self.y + self.card_height
        ):
            self.is_flipped = not self.is_flipped  # Flip the card state

# Example of use
# def main():
#     # Initialize Pygame
#     pygame.init()

#     # Set screen size
#     screen_width = 800
#     screen_height = 600
#     screen = pygame.display.set_mode((screen_width, screen_height))
#     pygame.display.set_caption("Flashcard App")

#     # Define some example questions and answers (replace with your data)
#     questions = ["What is the capital of France?", "What is 2 + 2?"]
#     answers = ["Paris", "4"]

#     # Create flashcards (distribute them on screen for better visuals)
#     flashcards = []
#     card_width = 200
#     card_height = 150
#     margin = 50  # Adjust spacing between cards
#     for i, (question, answer) in enumerate(zip(questions, answers)):
#         x = margin + (i % 2) * (
#             card_width + margin
#         )  # Alternate positions for 2 cards per row
#         y = margin + (i // 2) * (
#             card_height + margin
#         )  # Adjust for multiple rows if needed
#         flashcards.append(FlashCard(question, answer, x, y, card_width, card_height))

#     # Game loop
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             # Handle mouse clicks on cards
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 for card in flashcards:
#                     card.handle_click(mouse_pos)

#         # Clear the screen
#         screen.fill(BLACK)

#         # Draw all flashcards
#         for card in flashcards:
#             card.draw(screen)

#         # Update the display
#         pygame.display.flip()

#     # Quit Pygame
#     pygame.quit()


# if __name__ == "__main__":
#     main()
