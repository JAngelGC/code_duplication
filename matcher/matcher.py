from difflib import SequenceMatcher
from lexer.lexer import Lexer

def get_match_plain_text(file_path_1: str, file_path_2: str):
    file_1 = _read_file(file_path_1)
    file_2 = _read_file(file_path_2)

    match = SequenceMatcher(None, file_1, file_2)
    print(match.ratio())


def get_match_preprocesses_text(file_path_1: str, file_path_2: str):
    tokens_file_1 = Lexer.get_tokens(file_path_1)
    print(tokens_file_1)
    

def _read_file(file_path):
    print(f'------------- {file_path}')
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise e