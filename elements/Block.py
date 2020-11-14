from bs4 import BeautifulSoup
from .Question import Question


class Block:
    def __init__(self, html, number, name):
        self.number = number
        self.name = name
        self.soup = BeautifulSoup(html, features="html.parser")
        self.questions = self.parse_questions()

    def parse_questions(self):
        questions_list_tag = self.soup.find("ol", class_="wpProQuiz_list")
        questions_tags = questions_list_tag.find_all("li", class_="wpProQuiz_listItem")
        questions = list(Question(q_tag) for q_tag in questions_tags)
        return questions

    def get_questions(self):
        return self.questions

    def get_json(self):
        return {'id': self.number,
                'name': self.name,
                'questions': list(q.get_json() for q in self.questions)}

    def __str__(self):
        return f'\n========== Блок {self.number} ==========\n' + \
               self.name + "\n\n" + \
               '\n\n'.join(list(str(q) for q in self.get_questions()))
