from pythonparser import source, lexer, diagnostic
from pathlib import Path
from typing import Union, List
import re



class Lexer:

    @staticmethod
    def get_tokens(filepath: Union[str, Path]):
        """
        Given a 'filepath', it returns an array of the tokens
        New: Given a 'filepath', it returns an string of the content of the
        file with its identifiers replaced.

        Returns:
            tokens: Array of tokens of the 'filepath'
        """
        buf = None
        with open(filepath) as f:
            buf = source.Buffer(f.read(), f.name)

        engine = diagnostic.Engine()

        tokens: List[lexer.Token] = []
        for token in lexer.Lexer(buf, (3, 4), engine):
            tokens.append(token)
        
        return tokens, buf

    def replace_ident(tokens, buf):
        rewriter = source.Rewriter(buf)
        in_quot  = False
        replace  = { "'": "\"", "'''": "\"\"\"" }

        for token in tokens:
            # print(token)
            source_ = token.loc.source()
            
            if token.kind == "ident":
                rewriter.replace(token.loc, "ident")

            if token.kind == "strbegin" and source_ in replace.keys():
                rewriter.replace(token.loc, replace[source_])
                in_quot = True
            elif token.kind == "strdata" and in_quot:
                rewriter.replace(token.loc, re.sub(r'([^\\"]|)"', r'\1\\"', source_))
            elif token.kind == "strend" and in_quot:
                rewriter.replace(token.loc, replace[source_])
                in_quot = False

        buf = rewriter.rewrite()
        return buf.source