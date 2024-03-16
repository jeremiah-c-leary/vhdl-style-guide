# -*- coding: utf-8 -*-

from vsg import parser


class subtype_keyword(parser.keyword):
    """
    unique_id = subtype_declaration : subtype_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = subtype_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = subtype_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = subtype_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
