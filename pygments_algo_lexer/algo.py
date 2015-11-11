# -*- coding: utf-8 -*-
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

    tokens = {
        'root': [
            (r'(module)(\s*)([^\s=]+)', bygroups(Keyword.Namespace, Text, Name.Namespace)),
            (r'(var)(\s*)([^\s:]+)', bygroups(Keyword.Declaration, Text, Name.Variable)),
            (r'\(\*', Comment.Multiline, 'comment'),
            (r'[\+=\|\.\*\;\?-]', Operator),
            (r'[\[\]\(\)\{\}]', Operator),
            (r'"', String.Double, 'string'),
            (r'\/', String.Regex, 'regex'),
            (r'([A-Z]\w*)(\.)(\w+)', bygroups(Name.Namespace, Punctuation, Name.Variable)),
            (r'.', Name.Variable),
            (r'\s', Text),
        ],
        'string': [
            (r'\\.', String.Escape),
            (r'[^"]', String.Double),
            (r'"', String.Double, '#pop'),
        ],
        'regex': [
            (r'\\.', String.Escape),
            (r'[^\/]', String.Regex),
            (r'\/', String.Regex, '#pop'),
        ],
        'comment': [
            (r'[^*\)]', Comment.Multiline),
            (r'[\*\)]', Comment.Single)
        ],
    }

