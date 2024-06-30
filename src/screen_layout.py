import pygame
import flash_cards

class SplitScreenLayout:
    def __init__(self, screen_width, screen_height, flashcards_from_file):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.section_ratio = 0.20  # 80% width for the right section

        # Title bar properties
        self.title_bar_height = 50  # Adjust as needed
        self.title_bar_margin = 5  # Margin between title bar and content
        self.title_bar_color = (89, 64, 203)  # Customize title bar color

        # Calculate section dimensions
        self.title_bar_rect = pygame.Rect(0, 0, screen_width, self.title_bar_height)
        self.title_text_margin = 10

         # Calculate remaining section dimensions
        self.menu_section_height = self.screen_height - self.title_bar_height - self.title_bar_margin
        self.menu_section_width = int(screen_width * self.section_ratio)
        self.menu_section_rect = pygame.Rect(0, self.title_bar_height + self.title_bar_margin, self.menu_section_width, self.menu_section_height)
        self.right_section_rect = pygame.Rect(self.menu_section_width, self.title_bar_height + self.title_bar_margin, screen_width - self.menu_section_width, self.screen_height - self.title_bar_height - self.title_bar_margin)
 
        # Button properties (customize as needed)
        self.button_width = 200
        self.button_height = 50
        self.button_margin = 10
        self.button_colors = [(200, 200, 255), (150, 150, 255)]  # Default and hover colors

        self.button_tag = ""

        self.flashcards_file = self.create_flash_cards(flashcards_from_file)
        self.flashcards = []

        # Initialize button states (False = not clicked, True = clicked)
        self.num_buttons = len(self.flashcards_file)

    def draw_cards(self, button, screen):
        self.load_flashcards(button.get_clicked_tag())  # Get flashcards based on clicked tag
        # Update current flashcard 
        self.flashcards = self.flashcards_file[self.button_tag] if self.button_tag != "" else []
        # Draw flashcard
        for flashcard_file in self.flashcards:
            flashcard_file.draw(screen)

    def draw(self, screen):
        # Draw the title bar
        pygame.draw.rect(screen, self.title_bar_color, self.title_bar_rect)
        font = pygame.font.Font(None, 32)  # Example font object
        title_left_text = "Code In Place 2024"
        text_left_surface = font.render(title_left_text, True, (255, 255, 255))  # White text
        text_rect = text_left_surface.get_rect()
        x_left = self.title_text_margin
        y_left = self.title_bar_rect.centery - text_rect.height // 2
        screen.blit(text_left_surface, (x_left, y_left))

        title_center_text = "Flashcards"
        text_center_surface = font.render(title_center_text, True, (255, 255, 255))  # White text
        text_rect = text_center_surface.get_rect()
        x_center = self.title_bar_rect.centerx - text_rect.width // 2
        y_center = self.title_bar_rect.centery - text_rect.height // 2
        screen.blit(text_center_surface, (x_center, y_center))

        # Draw the split sections
        pygame.draw.rect(screen, (255, 255, 255), self.menu_section_rect)  # Customize menu section color
        pygame.draw.rect(screen, (220, 220, 220), self.right_section_rect)  # Customize right section color
    
    def create_flash_cards(self, flashcards_from_file):
        flashcards_file = {}

        for flashcard_key in flashcards_from_file:
            flashcards = []
            card_width = 210
            card_height = 150
            margin = 20
            # Track the current row's x position (starts at margin)
            current_row_x = self.right_section_rect.left + margin
            for flashcard in flashcards_from_file[flashcard_key]:
                # Check if there's enough space for the card in the current row
                if current_row_x + card_width + margin > self.right_section_rect.right:
                    # Move to the next row (reset x and adjust y)
                    current_row_x = self.right_section_rect.left + margin
                    y = flashcards[-1].y + card_height + margin if flashcards else margin  # Start at top or below last card
                else:
                    y = margin # Start from top for the first card in a row
                flashcard_draw = flash_cards.FlashCard(flashcard["question"], flashcard["answer"], current_row_x, y, self.title_bar_height, card_width, card_height)
                flashcards.append(flashcard_draw)
                # Update current_row_x for the next card in the same row
                current_row_x += card_width + margin
            flashcards_file[flashcard_key] = flashcards
        return flashcards_file

    def handle_button_click(self, mouse_pos, button):
        # Check click within button rect for each button
        tag_flashcard = button.handle_button_click(mouse_pos)
        if tag_flashcard:    
            # if self.flashcards:  # Clear only if flashcards exist
            #     self.flashcards.clear()
            # Optionally, load or generate flashcards based on button index (i)
            self.load_flashcards(tag_flashcard)  # Replace with your logic

    def load_flashcards(self, button_tag):
        if button_tag:
           #self.flashcards = self.flashcards_file[button_tag]
           self.button_tag = button_tag

