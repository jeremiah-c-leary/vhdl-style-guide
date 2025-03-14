# -*- coding: utf-8 -*-

from vsg import parser


class restrict_n_keyword(parser.keyword):
    """
    unique_id = psl_restrict_n_directive : restrict_n_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_restrict_n_directive : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = psl_restrict_n_directive : semicolon
    """

    def __init__(self, sString):
        super().__init__()
