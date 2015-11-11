# -*- coding: iso8859-15 -*-
"""
    pygments.lexers.algo
    ~~~~~~~~~~~~~~~~~~~

    Custom lexers for GitHub.com

    :copyright: Copyright 2012 by GitHub, Inc
    :license: BSD, see LICENSE for details.
"""
import re

from pygments.lexer import RegexLexer, ExtendedRegexLexer, include, bygroups, \
    using, DelegatingLexer
from pygments.token import Text, Name, Number, String, Comment, Punctuation, \
     Other, Keyword, Operator, Literal, Whitespace

__all__ = ['AlgoLexer']

class AlgoLexer(RegexLexer):
    """
    Simple lexer for "algo" algorithmic interpreter
    """
    name = 'algo'
    aliases = ['Algo']
    filenames = ['*.alg']
    mimetypes = ['text/plain']

    flags = re.IGNORECASE | re.DOTALL

    tokens = {
        'root': [
            include('whitespace'),
            (r'(algorithme)(\s*)([^\s]+)',bygroups(Keyword, Text, Name)),
            (r'\(\*', Comment.Multiline, 'comment'),
            (r'(fonction)(\s*)\(([^\s]+)\):([^\s]+)',bygroups(Keyword, Text, Name.Function, Keyword.Type)),
            (r'entier|réel|chaîne|car|booléen',Keyword.Type),
            (r'var',Keyword.Declaration),
            (r'([^\s]+)(\s*)(:)',bygroups(Name.Variable, Text, Operator)),
            (r'début',Keyword.Reserved,'block'),
            (r'"',String.Double, 'string'),
            (r',',Punctuation)
        ],
        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
        ],
        'string': [
            (r'\\.', String.Escape),
            (r'[^"]', String.Double),
            (r'"', String.Double, '#pop'),
        ],
        'comment': [
            (r'[^*\)]', Comment.Multiline),
            (r'\(\*', Comment.Multiline, '#push'),
            (r'\*\)', Comment.Multiline, '#pop'),
            (r'[\*\)]', Comment.Multiline)
        ],
        'block':[
            (r'fin',Keyword.Reserved,'#pop')
        ]
    }

