# CIP_2024_Flash_Cards

## Create python virtual environment
* `python3 -m venv my_neovim_env` (created if not exist, if exist next step)
* `source my_neovim_env/bin/activate`

## Install requirements 
* `pip3 install pygame`
* `pip3 install -r requirements.txt`

## Execute project
* `python3 ./src/main.py`

![Watch the video](https://youtu.be/7hGUeGCf4Mo)

## Considerations:
* The flashcards hasn't have dynamic height. Questions and answers should be brief.
* To put your own flahscard information should be in the `card_data/my_flash_cards.txt` file.

## Next Steps

- [ ] Upload of `.txt` files for new flashcard information.
- [ ] Button to clean cards in the screen.
- [ ] Update status of flip card when the context change. (ex: from for loop to while loop).