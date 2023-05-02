import json
from gendiff.generate_diff import generate_diff as gd
from gendiff.generate_diff import create_formatted_diff as cfd


FIRST_FILE_PATH = "tests//fixtures//plain_file1.json"
SECOND_FILE_PATH = "tests//fixtures//plain_file2.json"
CORRECT_FILE_PATH = "tests//fixtures//correct_plain_json.json"
EMPTY_FILE_PATH = "tests//fixtures//empty_json.json"
with open(FIRST_FILE_PATH) as file1, open(SECOND_FILE_PATH) as file2:
    first_file = json.load(file1)
    second_file = json.load(file2)
with open(CORRECT_FILE_PATH) as correct_file:
    correct_file = correct_file.read()
with open(EMPTY_FILE_PATH) as empty_file:
    empty_file = empty_file.read()


def test_create_formatted_diff_same_files():
    file1 = {'a': 1, 'b': 2, 'c': 3}
    file2 = {'a': 1, 'b': 2, 'c': 3}
    expected_output = {
        '  a': 1,
        '  b': 2,
        '  c': 3
    }
    assert cfd(file1, file2) == expected_output


def test_create_formatted_diff_one_empty_file():
    file1 = {}
    file2 = {'a': 1, 'b': 2, 'c': 3}
    expected_output = {
        '+ a': 1,
        '+ b': 2,
        '+ c': 3
    }
    assert cfd(file1, file2) == expected_output


def test_create_formatted_diff():
    assert cfd(first_file, second_file) == {
        '- follow': False,
        '  host': 'hexlet.io',
        '- proxy': '123.234.53.22',
        '- timeout': 50,
        '+ timeout': 20,
        '+ verbose': True
    }
    assert cfd({}, {}) == {}


def test_generate_diff():
    assert gd(FIRST_FILE_PATH, SECOND_FILE_PATH) == correct_file
    assert gd(EMPTY_FILE_PATH, EMPTY_FILE_PATH) == empty_file
