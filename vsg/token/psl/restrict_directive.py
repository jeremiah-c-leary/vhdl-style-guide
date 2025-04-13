# -*- coding: utf-8 -*-

from vsg import parser


class restrict_keyword(parser.keyword):
    """
    unique_id = psl_restrict_directive : restrict_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_restrict_directive : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = psl_restrict_directive : semicolon
    """

    def __init__(self, sString):
        super().__init__()
