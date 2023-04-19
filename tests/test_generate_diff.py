import json
from difference_calculator.generate_diff import generate_diff as gd
from difference_calculator.generate_diff import create_formatted_diff as cfd


FIRST_FILE_PATH = "tests//fixtures//plain_file1.json"
SECOND_FILE_PATH = "tests//fixtures//plain_file2.json"
CORRECT_FILE_PATH = "tests//fixtures//correct_plain_json.json"
with open(FIRST_FILE_PATH) as file1, open(SECOND_FILE_PATH) as file2:
    FIRST_FILE = json.load(file1)
    SECOND_FILE = json.load(file2)
with open(CORRECT_FILE_PATH) as correct_file:
    CORRECT_FILE = correct_file.read()


def test_create_formatted_diff():
    assert cfd(FIRST_FILE, SECOND_FILE) == {
        '- follow': False, 
        '  host': 'hexlet.io', 
        '- proxy': '123.234.53.22', 
        '- timeout': 50, 
        '+ timeout': 20, 
        '+ verbose': True
    }
    assert cfd({}, {}) == {}


def test_generate_diff(): 
    gd(FIRST_FILE_PATH, SECOND_FILE_PATH) == CORRECT_FILE
