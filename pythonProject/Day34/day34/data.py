import requests


class Data:
    def __init__(self):
        self.response = requests.get(url="https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean")
        self.response.raise_for_status()
        self.questions = self.response.json()["results"]
        print(self.questions)
        self.correct = 0
        self.answered = 0


# Data()

