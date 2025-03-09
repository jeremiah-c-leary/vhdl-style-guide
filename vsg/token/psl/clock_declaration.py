# -*- coding: utf-8 -*-

from vsg import parser


class default_keyword(parser.keyword):
    """
    unique_id = psl_clock_declaration : default_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class clock_keyword(parser.keyword):
    """
    unique_id = psl_clock_declaration : clock_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_clock_declaration : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = psl_clock_declaration : semicolon
    """

    def __init__(self, sString):
        super().__init__()
