from pythonparser import source, lexer, diagnostic
from pathlib import Path
from typing import Union, List
import re


class Lexer:

    @staticmethod
    def get_tokens(filepath: Union[str, Path]):
        """
        Given a 'filepath', it returns an array of its tokens

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

    def replace_ident(tokens: List[lexer.Token], buf: source.Buffer):
        """
        Given a list of tokens and a buffer, it replaces all identifieres
        for a common string 'ident'

        Input:
            tokens: List of tokens
            buf: Buffer containing the plain text of the tokens
        """
        rewriter = source.Rewriter(buf)
        in_quot  = False
        replace  = { "'": "\"", "'''": "\"\"\"" }

        for token in tokens:
            source_ = token.loc.source()
            
            # replace identifiers fr 'ident'
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