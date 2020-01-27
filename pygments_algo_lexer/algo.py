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
    aliases = ['Algo','algo']
    filenames = ['*.algo']
    mimetypes = ['text/plain']

    flags = re.IGNORECASE | re.DOTALL

    stringIdentifierRegex = \
        r'[\xC0\xC2\xC6-\xCB\xCE\xCF\xD4\xD9\xDB\xDC\xE0\xE2\xE6-\xEB\xEE\xEF\xF4\xF9\xFB\xFC\xFFa-zA-Z_0-9]+'

    tokens = {
        'root': [
            include('headers'),
            include('comment'),
            include('data'),
            include('operators'),
            include('ponctuation'),
            include('keywords'),
            include('functions'),
            include('whitespace'),
            include('variables'),
            include('builtins')
        ],
        'ponctuation': [
            (r'(,|;|\(|\)|\[|\]|\.)',Punctuation)
        ],
        'headers': [
            (r'(algorithme)(\s*)('+stringIdentifierRegex+')',bygroups(Keyword, Text, Name)),
            (r'(fonction)(\s*)('+stringIdentifierRegex+')',bygroups(Keyword, Text, Name.Function)),
            (r'(proc\xE9dure)(\s*)('+stringIdentifierRegex+')',bygroups(Keyword, Text, Name.Function)),
            (r'(d\xE9but)(\s*)(fin)',bygroups(Keyword, Text, Keyword)),
        ],
        'keywords': [
            (r'\bsinon|fin si|fin tant que|fin pour|jusqu\'\xE0|tant que|faire|selon|pour|de|\xE0|si|alors|retourne\b', Keyword.Reserved),
            (r'\bentier|r\xE9el|cha\xEEne|tableau|bool\xE9en\b',Keyword.Type),
            (r'\bvariables\b',Keyword.Declaration),
        ],
        'builtins': [
            (r'\blire|\xE9crire\b', Name.Builtin),
        ],
        'functions': [
            (r'('+stringIdentifierRegex+')(\s*)(\()', bygroups(Name.Function,Text,Punctuation))
        ],
        'variables': [
            (stringIdentifierRegex, Name),
        ],
        'data': [
            (r"'",String.Simple, 'simple-quoted-strings'),
            (r'(\d\.\d)',Number.Float),
            (r'\d',Number.Integer),
        ],
        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
        ],
        'simple-quoted-strings': [
            (r'\\.', String.Escape),
            (r"[^']", String.Simple),
            (r"'", String.Simple, '#pop'),
        ],
        'comment': [
            (r'\/\*', Comment.Multiline, 'commentblock'),
            (r'--([^\n]*)', Comment.Single)
        ],
        'commentblock': [
            (r'[^*\/]', Comment.Multiline),
            (r'\/\*', Comment.Multiline, '#push'),
            (r'\*\/', Comment.Multiline, '#pop'),
            (r'[\*\/]', Comment.Multiline)
        ],
        'operators':[
            (r'(<-|=|>|<|:|\+|-|/|\^)',Operator),
            (r'\b(et|ou|non|div|mod)\b',Operator.Word)
        ]
    }
