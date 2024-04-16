from pythonparser import source, lexer, diagnostic
from pathlib import Path
from typing import Union

class Lexer:

    @staticmethod
    def get_tokens(filepath: Union[str, Path]):
        """
        Given a 'filepath', it returns an array of the tokens

        Returns:
            tokens: Array of tokens of the 'filepath'
        """
        engine = diagnostic.Engine()
        buf = None
        with open(filepath) as f:
            buf = source.Buffer(f.read(), f.name)

        tokens = []
        for token in lexer.Lexer(buf, (3, 4), engine):
            tokens.append(token)
        
        return tokens

