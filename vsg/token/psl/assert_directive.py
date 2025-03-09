# -*- coding: utf-8 -*-

from vsg import parser


class assert_keyword(parser.keyword):
    """
    unique_id = psl_assert_directive : assert_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_assert_directive : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = psl_assert_directive : semicolon
    """

    def __init__(self, sString):
        super().__init__()
