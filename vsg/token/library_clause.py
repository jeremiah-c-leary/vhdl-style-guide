# -*- coding: utf-8 -*-

from vsg import parser


class keyword(parser.keyword):
    """
    unique_id = library_clause : keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = library_clause : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
