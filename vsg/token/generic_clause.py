# -*- coding: utf-8 -*-

from vsg import parser


class generic_keyword(parser.keyword):
    """
    unique_id = generic_clause : generic_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = generic_clause : open_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = generic_clause : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = generic_clause : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
