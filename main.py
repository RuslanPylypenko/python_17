import requests
import json
from datetime import datetime

MIN_PARAGRAPHS = 5
SEARCH_WORD = 'Pancetta'
FILE_PATH = './storage/result.txt'


def read_count_of_paragraphs():
    paragraphs = int(input("Enter count of paragraphs: "))
    return paragraphs if paragraphs >= MIN_PARAGRAPHS else read_count_of_paragraphs()


def load_data():
    url = 'https://baconipsum.com/api/?type=meat-and-filler&paras={}&format=json'.format(read_count_of_paragraphs())
    r = requests.get(url)
    return json.loads(r.content)


def write_report(file_path, *data_items):
    with open(file_path, 'w') as f:
        for item in data_items:
            f.write(formatter(item))
            f.write('\n' + '=' * 300 + '\n')


def formatter(data):
    text = ''
    if isinstance(data, type({})):
        for key, value in data.items():
            text += '{}: {}\n'.format(key, value)
        return text
    return '\n\n'.join(list(data))


list_of_paragraphs = load_data()

list_of_paragraphs_reversed = list_of_paragraphs[::-1]

count_paragraphs_with_word = len(list(filter(lambda p: p.find(SEARCH_WORD) != -1, list_of_paragraphs)))

result = {"name": "Ruslan", "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
          "searched_words": count_paragraphs_with_word}


write_report(FILE_PATH, result, list_of_paragraphs_reversed)
