import pygame
import flash_cards

class SplitScreenLayout:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.section_ratio = 0.25  # 70% width for the right section

        # Calculate section dimensions
        self.menu_section_width = int(screen_width * self.section_ratio)
        self.menu_section_rect = pygame.Rect(0, 0, self.menu_section_width, screen_height)
        self.right_section_rect = pygame.Rect(self.menu_section_width, 0, screen_width - self.menu_section_width, screen_height)

    def draw_cards(self):
        flashcards = []
        questions = ["What is the capital of France?", "What is 2 + 2?"]
        answers = ["Paris", "4"]
        card_width = 150
        card_height = 100
        margin = 20
        # Track the current row's x position (starts at margin)
        current_row_x = self.right_section_rect.left + margin

        for question, answer in zip(questions, answers):
            # Check if there's enough space for the card in the current row
            if current_row_x + card_width + margin > self.right_section_rect.right:
                # Move to the next row (reset x and adjust y)
                current_row_x = self.right_section_rect.left + margin
                y = flashcards[-1].y + card_height + margin if flashcards else margin  # Start at top or below last card
            else:
                y = margin  # Start from top for the first card in a row

            flashcard = flash_cards.FlashCard(question, answer, current_row_x, y, card_width, card_height)
            flashcards.append(flashcard)

            # Update current_row_x for the next card in the same row
            current_row_x += card_width + margin

        return flashcards

    def draw(self, screen, flashcards):
        # Draw the split sections
        pygame.draw.rect(screen, (200, 200, 200), self.menu_section_rect)  # Customize menu section color
        pygame.draw.rect(screen, (220, 220, 220), self.right_section_rect)  # Customize right section color


        # for event in pygame.event.get():
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         mouse_pos = pygame.mouse.get_pos()  # Get mouse position
        #         for card in flashcards:
        #             card.handle_click(mouse_pos)

        # # Draw all flashcards on the screen
        # for card in flashcards:
        #     card.draw(screen)




# Example usage
if __name__ == "__main__":
    pygame.init()
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flashcard - CIP")

    layout = SplitScreenLayout(screen_width, screen_height)
    flashcards = layout.draw_cards()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get mouse position
                for card in flashcards:
                    card.handle_click(mouse_pos)


        screen.fill((255, 255, 255))  # Fill background with white
        layout.draw(screen, flashcards)
        # Draw all flashcards on the screen
        for card in flashcards:
            card.draw(screen)
        
        
        #Update the display
        pygame.display.flip()

    pygame.quit()
