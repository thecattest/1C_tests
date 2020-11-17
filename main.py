import elements
import os
import json

block_titles = {1: 'Общие механизмы, понятия и термины 1С',
                2: 'Редакторы и инструменты 1С (общие)',
                3: 'Редакторы и инструменты режима разработки 1С',
                4: 'Конструкторы 1С', 5: 'Технология разработки 1С',
                6: 'Объектная модель прикладного решения 1С',
                7: 'Табличная модель прикладного решения 1С',
                8: 'Механизмы интеграции и обмена данными в 1С',
                9: 'Обслуживание прикладного решения 1С',
                10: 'Интерфейсные механизмы 1С',
                11: 'Механизмы построения отчетности 1С',
                12: 'Механизмы оперативного учета 1С',
                13: 'Объекты и механизмы бухгалтерского учета 1С',
                14: 'Механизмы сложных периодических расчетов 1С'}


def save_html_to_json(html_dir, json_dir):
    html_names = os.listdir(html_dir)
    blocks = []
    for html_name in html_names:
        block_id = int(html_name.split('.')[0])
        block_name = block_titles[block_id]

        html_path = os.path.join(html_dir, html_name)
        print(f"Loading {html_path}...")
        with open(html_path) as html_file:
            html = html_file.read()

        print("Parsing...")
        block = elements.Block(html, block_id, block_name)
        blocks.append(block)

        json_path = os.path.join(json_dir, str(block.number) + ".json")
        print(f"Saving json to {json_path}...")
        with open(json_path, 'wt') as file:
            json.dump(block.get_json(), file)
        print("Ok\n===\n")

    return blocks


def question_json_to_gift(q_json):
    q_gift = str(q_json["id"]) + ". "
    q_gift += q_json["title"]
    if "img" in q_json:
        q_gift += "\n&&&"
        q_gift += os.path.join("img", q_json["img"])
        q_gift += "&&&\n"
    q_gift += "{\n"
    for i in range(len(q_json["answers"])):
        answer = q_json["answers"][i]
        if answer[1]:
            q_gift += "="
        else:
            q_gift += "~"
        q_gift += str(i+1) + ". "
        q_gift += answer[0]
        q_gift += '\n'
    q_gift += "}\n"
    return q_gift


def save_json_to_gift(json_dir, gift_dir):
    json_names = os.listdir(json_dir)
    for json_name in json_names:
        json_path = os.path.join(json_dir, json_name)
        print(f"Loading {json_path}...")
        with open(json_path) as file:
            block = json.load(file)

        print("Wrapping a gift...")
        gift_content = f"1C_{block['id']}#{block['id']}. {block['name']}###\n"
        for q in block['questions']:
            gift_content += question_json_to_gift(q)

        gift_path = os.path.join(gift_dir, str(block["id"]) + ".txt")
        print(f"Saving gift to {gift_path}...")
        with open(gift_path, 'wt') as file:
            file.write(gift_content)
        print("Ok\n===\n")


if __name__ == '__main__':
    html_dir_path = os.path.join("src", "html")
    json_dir_path = os.path.join("src", "json")
    gift_dir_path = os.path.join("src", "gift")

    # save_html_to_json(html_dir_path, json_dir_path)
    save_json_to_gift(json_dir_path, gift_dir_path)
