"""
    test_duplication.py

    In the future, pytest will be used
"""

from matcher.matcher import get_match_plain_text, get_match_preprocesses_text
from files.files import get_absolute_file_path


file_paths = get_absolute_file_path()

def test_plain_text(file_path_1, file_path_2):
    get_match_plain_text(file_path_1, file_path_2)


def test_preprocessed_text(file_path_1, file_path_2):
    get_match_preprocesses_text(file_path_1, file_path_2)

test_plain_text(file_paths[0], file_paths[1])
get_match_preprocesses_text(file_paths[0], file_paths[1])


