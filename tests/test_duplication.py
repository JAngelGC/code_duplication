"""
    test_duplication.py

    In the future, pytest will be used
"""

from matcher.matcher import print_match_plain_text, print_match_preprocesses_text
from files.files import get_absolute_file_path
from typing import List

# Store all test files
file_paths: List[str] = get_absolute_file_path()
file_paths.sort()

def test_match_plain_text(file_path_1, file_path_2):
    test_name = "Test: Match no-preprocessed texts"
    print("\n-------------------------------")
    print(test_name)
    print_match_plain_text(file_path_1, file_path_2)


def test_match_preprocessed_texts(file_path_1, file_path_2):
    test_name = "Test: Match preprocessed texts"
    print("\n-------------------------------")
    print(test_name)
    print_match_preprocesses_text(file_path_1, file_path_2)


# Tests
pairs_of_files: List[List[str]] = [
    [file_paths[0], file_paths[1]],
    [file_paths[2], file_paths[3]],
    [file_paths[0], file_paths[3]],
    [file_paths[4], file_paths[5]]
]

for pair_of_files in pairs_of_files:
    test_match_plain_text(pair_of_files[0], pair_of_files[1])
    test_match_preprocessed_texts(pair_of_files[0], pair_of_files[1])
