from difflib import SequenceMatcher
from lexer.lexer import Lexer
from pythonparser.lexer import Token
from typing import List
from pythonparser import source

def print_match_plain_text(file_path_1: str, file_path_2: str):
    """
    """
    content_file_1: str = _read_file(file_path_1)
    content_file_2: str = _read_file(file_path_2)

    match = SequenceMatcher(None, content_file_1, content_file_2)
    match_percentage: int = int(match.ratio() * 100)

    print(f"Matching {file_path_1} to {file_path_2}")
    print(f"Match percentage is {match_percentage}%")
    print_similar_lines(content_file_1, content_file_2)


def print_match_preprocesses_text(file_path_1: str, file_path_2: str):
    """
    Prints match percentage of similarity between files 'file_path_1' and
    'file_path_2'

    Input:
        file_path_1: Absolute path of file 1
        file_path_2: Absolute path of file 2
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

    print(f"Matching {file_path_1} to {file_path_2}")
    print(f"Match percentage is {match_percentage}%")
    print_similar_lines(content_file_1, content_file_2)


def print_similar_lines(file_content_1: str, file_content_2: str):
    """
    Given 'file_content_1' and 'file_content_2', it prints the lines
    that are in both files.

    The content is already preprocess replacing identifieres for a common value.

    Input:
        file_content_1: Content of file 1
        file_content_2: Content of file 2    
    """
    lines_file_1: List[str] = file_content_1.splitlines()
    lines_file_2: List[str] = file_content_2.splitlines()
    similar_lines: List[List] = []
    count: int = 0

    for i in range(0, len(lines_file_1)):
        line_shortet_file = lines_file_1[i]
        for j in range(0, len(lines_file_2)):
            # line in both files and it is not \n
            if line_shortet_file == lines_file_2[j] and line_shortet_file.strip():
                count += 1
                similar_lines.append([i, j])
                break
    
    if len(similar_lines) > 0:
        print("Similar lines in files") 
    for line in similar_lines:
        print(f"File 1 Ln {line[0]+1} is very similar to File 2 Ln {line[1]+1}")

def _read_file(file_path: str):
    """
    Given a 'file_path' it opens the file and reads its content.

    Input:
        file_path: Absolute path of the file
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError as e:
        raise e
    except Exception as e:
        raise e