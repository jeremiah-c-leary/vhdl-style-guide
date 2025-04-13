# -*- coding: utf-8 -*-

from vsg import parser


class property_keyword(parser.keyword):
    """
    unique_id = psl_property_declaration : property_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_property_declaration : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = psl_property_declaration : semicolon
    """

    def __init__(self, sString):
        super().__init__()
