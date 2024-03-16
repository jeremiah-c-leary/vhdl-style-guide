# -*- coding: utf-8 -*-

from vsg import parser


class keyword(parser.keyword):
    """
    unique_id = type_declaration : keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = type_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class type_definition(parser.item):
    """
    unique_id = type_declaration : type_definition
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = type_declaration : semicolon
    """

    def __init__(self):
        super().__init__()
