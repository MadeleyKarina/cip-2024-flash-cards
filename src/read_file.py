# read file
import os
class DataReader:
    def __init__(self, folder, filename, data_type="string"):
        self.folder_name = folder
        self.filename = filename
        self.data_type = data_type
        self.data = {}

    def read_flashcards_from_file(self):
        # Get the current working directory
        current_dir = os.getcwd()
        
        file_path = os.path.join(current_dir,"src",self.folder_name,self.filename)
        with open(file_path, "r") as file:
            file_contents = file.readlines()

        flashcards = {}

        for line in file_contents:
            if not line.strip():
                continue

            # Split each line by the question mark separator
            tag_question, answer = line.strip().split(":")
            if not tag_question or not answer:
                continue
            
            tag, question = tag_question.strip().split("-")
            if not tag or not question:
                continue

            flashcard = {"question": " ".join(question.strip().split()), "answer": " ".join(answer.strip().split())}
            tag = tag.strip()
            if tag in flashcards:
                flashcards[tag].append(flashcard)
            else:
                flashcards[tag] = [flashcard]

        return flashcards

