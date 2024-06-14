import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font size for text
FONT_SIZE = 30


class FlashCard:
    def __init__(self, question, answer, x, y, width, height):
        self.question = question

        self.answer = answer
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if (
            pygame.font is not None
        ):  # Check if pygame.font is available (indirect init check)
            self.font = pygame.font.SysFont(None, FONT_SIZE)
        else:
            print("Warning: Pygame might not be initialized. Font creation might fail.")

        # self.font = pygame.font.SysFont(None, FONT_SIZE)

        # Text surfaces for question and answer (pre-render for efficiency)
        self.question_surface = self.font.render(self.question, True, BLACK)
        self.answer_surface = self.font.render(self.answer, True, BLACK)

        self.is_flipped = False  # Track if the card is flipped

    def draw(self, screen):
        # Draw a rectangle for the card
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height))

        # Display question or answer based on flipped state
        if self.is_flipped:
            screen.blit(
                self.answer_surface, (self.x + 10, self.y + 10)
            )  # Adjust positioning for padding
        else:
            screen.blit(self.question_surface, (self.x + 10, self.y + 10))

    def handle_click(self, pos):
        # Check if click is within the card's boundaries
        if (
            self.x < pos[0] < self.x + self.width
            and self.y < pos[1] < self.y + self.height
        ):
            self.is_flipped = not self.is_flipped  # Flip the card state


def main():
    # Initialize Pygame
    pygame.init()

    # Set screen size
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flashcard App")

    # Define some example questions and answers (replace with your data)
    questions = ["What is the capital of France?", "What is 2 + 2?"]
    answers = ["Paris", "4"]

    # Create flashcards (distribute them on screen for better visuals)
    flashcards = []
    card_width = 200
    card_height = 150
    margin = 50  # Adjust spacing between cards
    for i, (question, answer) in enumerate(zip(questions, answers)):
        x = margin + (i % 2) * (
            card_width + margin
        )  # Alternate positions for 2 cards per row
        y = margin + (i // 2) * (
            card_height + margin
        )  # Adjust for multiple rows if needed
        flashcards.append(FlashCard(question, answer, x, y, card_width, card_height))

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Handle mouse clicks on cards
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for card in flashcards:
                    card.handle_click(mouse_pos)

        # Clear the screen
        screen.fill(BLACK)

        # Draw all flashcards
        for card in flashcards:
            card.draw(screen)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
