import csv
import json
import os
from json import JSONDecodeError


def read_csv(path: str, delimiter: str):
    assert os.path.exists(path), "File does not exist"

    file_reader = csv.DictReader(open(path, encoding='utf-8'), delimiter=delimiter)

    assert file_reader.line_num == 0, "File is empty"

    return list(file_reader)


def read_json(path: str):
    assert os.path.exists(path), "File does not exist"

    with open(path) as file:
        try:
            result = json.load(file)
            return result
        except JSONDecodeError as error:
            print(f'File reading error:\n{error}')


def write_json(file_name: str, data):
    with open(f'{file_name}.json', 'w') as outfile:
        json.dump(data, outfile)
