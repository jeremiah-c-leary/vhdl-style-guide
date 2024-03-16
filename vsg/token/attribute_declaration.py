# -*- coding: utf-8 -*-

from vsg import parser


class attribute_keyword(parser.keyword):
    """
    unique_id = attribute_declaration : attribute_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = attribute_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = attribute_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = attribute_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
