# read file
import os
class DataReader:
    def __init__(self, filename, data_type="string"):
        self.filename = filename
        self.data_type = data_type
        self.data = {}

    def read_data(self):
        # Get the current working directory
        current_dir = os.getcwd()

        # Construct a path to the file (assuming a subdirectory named "data" and a file named "data.txt")
        filepath = os.path.join(current_dir, "src", self.filename)

        with open(filepath, "r") as file:
            if self.data_type == "string":
                for line in file:
                    clean_line = line.strip()
                    target_question = clean_line.split("-")

                    if len(target_question) != 2:
                        continue

                    target_card = " ".join(target_question[0].split())
                    question_answer = " ".join(target_question[1].split())

                    question, answer = question_answer.split("?")

                    question = " ".join(question.split())
                    answer = " ".join(answer.split())

                    if len(question) == 0 or len(answer) == 0:
                        continue

                    print(target_card, question, answer)

                    if target_card in self.data:
                        self.data[target_card].append(
                            {"question": question, "answer": answer}
                        )
                    else:
                        self.data[target_card] = [
                            {"question": question, "answer": answer}
                        ]
            else:
                raise ValueError(f"Unsupported data type: {self.data_type}")

    def get_data(self):
        if not self.data:
            raise RuntimeError("Data not yet read. Call read_data() first.")
        return self.data


data_reader = DataReader("my_flash_cards.txt")  # Read as integer
data_reader.read_data()
data = data_reader.get_data()
print(f"Read data: {data}")
