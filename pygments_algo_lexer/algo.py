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

    stringIdentifierRegex = r'[\xC0-\xD6\xD8-\xF6\xF8-\xFFa-zA-Z_][\xC0-\xD6\xD8-\xF6\xF8-\xFFa-zA-Z0-9_]*'

    tokens = {
        'root': [
            include('headers'),
            include('comment'),
            include('data'),
            include('ponctuation'),
            include('keywords'),
            include('functions'),
            include('operators'),
            include('whitespace'),
            include('variables'),
        ],
        'ponctuation': [
            (r'(,|;|\(|\))',Punctuation)
        ],
        'headers': [
            (r'(algorithme)(\s*)('+stringIdentifierRegex+')',bygroups(Keyword, Text, Name)),
            (r'(fonction)(\s*)('+stringIdentifierRegex+')',bygroups(Keyword, Text, Name.Function)),
            (r'(proc\xE9dure)(\s*)('+stringIdentifierRegex+')',bygroups(Keyword, Text, Name.Function)),
        ],
        'keywords': [
            (r'\bd\xE9but|sinon|fin|tant que|faire|selon|pour|de|\xE0|si|alors\b', Keyword.Reserved),
            (r'\bin|ex|entier|r\xE9el|chaîne|car|bool\xE9en\b',Keyword.Type),
            (r'\bvar\b',Keyword.Declaration),
            (r'\bfdl\b',Keyword.Constant)
        ],
        'functions': [
            (r'('+stringIdentifierRegex+')(\s*)(\()', bygroups(Name.Function,Text,Punctuation))
        ],
        'variables': [
            (stringIdentifierRegex, Name.Variable),
        ],
        'data': [
            (r'"',String.Double, 'string'),
            (r'(\')([^\'])(\')',bygroups(String.Simple, Text, String.Simple)),
            (r'(\d\.\d)',Number.Float),
            (r'\d',Number.Integer),
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
            (r'\(\*', Comment.Multiline, 'commentblock'),
            (r'--([^\n]*)', Comment.Single)
        ],
        'commentblock': [
            (r'[^*\)]', Comment.Multiline),
            (r'\(\*', Comment.Multiline, '#push'),
            (r'\*\)', Comment.Multiline, '#pop'),
            (r'[\*\)]', Comment.Multiline)
        ],
        'operators':[
            (r'(<-|/=|=|>|<|:|\+|-|/)',Operator),
            (r'(et|ou|non|div|mod)',Operator.Word)
        ]
    }

