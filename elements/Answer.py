class Answer:
    def __init__(self, tag):
        self.tag = tag
        self.title = self.get_title()
        self.is_correct = self.get_is_correct()

    def get_title(self):
        return self.tag.find("label").contents[-1].strip()

    def get_is_correct(self):
        return 'wpProQuiz_answerCorrect' in self.tag['class']

    def get_json(self):
        return [self.title, self.is_correct]

    def __str__(self):
        return self.title + " -- " + str(self.is_correct)