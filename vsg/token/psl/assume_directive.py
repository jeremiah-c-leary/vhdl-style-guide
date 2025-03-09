# -*- coding: utf-8 -*-

from vsg import parser


class assume_keyword(parser.keyword):
    """
    unique_id = psl_assume_directive : assume_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_assume_directive : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = psl_assume_directive : semicolon
    """

    def __init__(self, sString):
        super().__init__()
