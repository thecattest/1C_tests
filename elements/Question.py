from .Answer import Answer
import requests
import os


class Question:
    def __init__(self, tag, auto_download=True):
        self.tag = tag
        self.auto_download = auto_download
        self.id = self.get_id()
        self.title_tag, self.title = self.get_title()
        self.img_name = self.get_img()
        self.answers = self.get_answers()

    def get_id(self):
        q_id = self.tag.find("h5").find("span").string
        return int(q_id)

    def get_title(self):
        q_title_tag = self.tag.find("div", class_="wpProQuiz_question_text").find("p")
        q_title = ''.join(filter(lambda q: q.__class__.__name__ == 'NavigableString' and q, q_title_tag.contents))
        return q_title_tag, q_title

    def get_img(self):
        a_tag = self.title_tag.find("a", class_="highslide-image")
        if a_tag is None:
            return
        img_tag = a_tag.find("img")
        if img_tag is None:
            return
        img_url = img_tag['src']
        if self.auto_download:
            img_name = self.download_img(img_url)
        else:
            img_name = img_url.split('/')[-1]
        return img_name

    def download_img(self, img_url):
        img_name = img_url.split('/')[-1]
        print(img_name)
        img_path = os.path.join("src", "img", img_name)
        with open(img_path, 'wb') as f:
            f.write(requests.get(img_url).content)
        return img_name

    def get_answers(self):
        q_answers_tags = self.tag.find_all("li", class_="wpProQuiz_questionListItem")
        q_answers = list(Answer(a_tag) for a_tag in q_answers_tags)
        return q_answers

    def get_json(self):
        q = dict()
        q['id'] = self.id
        q['title'] = self.title
        if self.img_name is not None:
            q['img'] = self.img_name
        q['answers'] = list(a.get_json() for a in self.answers)
        return q

    def __str__(self):
        representation = str(self.id) + ": " + self.title
        if self.img_name is not None:
            representation += "\n(" + self.img_name + ")"
        representation += "\n* " + '\n* '.join(map(str, self.answers))
        return representation
