from difflib import SequenceMatcher
from lexer.lexer import Lexer
from pythonparser.lexer import Token
from typing import List
from pythonparser import source

def get_match_plain_text(file_path_1: str, file_path_2: str):
    """
    """
    file_1 = _read_file(file_path_1)
    file_2 = _read_file(file_path_2)

    match = SequenceMatcher(None, file_1, file_2)
    print(match.ratio())


def get_match_preprocesses_text(file_path_1: str, file_path_2: str):
    """
    """
    tokens_file_1: List[Token]
    tokens_file_2: List[Token]
    buf_file_1: source.Buffer
    buf_file_2: source.Buffer

    tokens_file_1, buf_file_1 = Lexer.get_tokens(file_path_1)
    content_file_1: str = Lexer.replace_ident(tokens_file_1, buf_file_1)

    tokens_file_2, buf_file_2 = Lexer.get_tokens(file_path_2)
    content_file_2: str = Lexer.replace_ident(tokens_file_2, buf_file_2)

    match = SequenceMatcher(None, content_file_1, content_file_2)
    match_percentage: int = int(match.ratio() * 100)
    print(match_percentage)

    print("*******************\n")
    print_similar_lines(content_file_1, content_file_2)


def print_similar_lines(str_1: str, str_2: str):
    lines_file_1: List[str] = str_1.splitlines()
    lines_file_2: List[str] = str_2.splitlines()
    similar_lines: List[List] = []
    count: int = 0

    for i in range(0, len(lines_file_1)):
        line_shortet_file = lines_file_1[i]
        for j in range(0, len(lines_file_2)):
            if line_shortet_file == lines_file_2[j] and line_shortet_file.strip():
                count += 1
                similar_lines.append([i, j])
                break
    
    print("Similar lines")
    for line in similar_lines:
        print(f"File 1 Ln {line[0]} is very similar to File 2 Ln {line[1]}")

    return similar_lines



def _read_file(file_path):
    """
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise e