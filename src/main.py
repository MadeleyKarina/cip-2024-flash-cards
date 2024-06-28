import pygame
import read_file
import screen_layout
import button

def main():
    pygame.init()
    screen_width = 1200
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Flashcard - CIP")

    data_reader = read_file.DataReader("card_data", "my_flash_cards.txt", ".txt")  # Read as integer
    flashcards_from_file =  data_reader.read_flashcards_from_file()
    flashcards_key = list(flashcards_from_file.keys())

    num_buttons = len(flashcards_from_file)
    
    layout = screen_layout.SplitScreenLayout(screen_width, screen_height, flashcards_from_file)
    button_menu = button.Button(layout.menu_section_width, layout.menu_section_rect, num_buttons)

    # layout.draw_cards(button, screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # Get mouse position
                layout.handle_button_click(mouse_pos, button_menu)
                for card in layout.flashcards:
                    card.handle_click(mouse_pos)


        screen.fill((255, 255, 255))  # Fill background with white

        layout.draw(screen)

        # Draw the menu section (buttons)
        for key in flashcards_from_file:
            idx = flashcards_key.index(key)
            button_menu.draw_buttons(screen, idx, key)
        
        # Draw all flashcards on the screen
        layout.draw_cards(button_menu, screen)

        #Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
