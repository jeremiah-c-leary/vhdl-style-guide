# -*- coding: utf-8 -*-

from vsg import parser


class port_keyword(parser.keyword):
    """
    unique_id = port_clause : port_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = port_clause : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = port_clause : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = port_clause : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
