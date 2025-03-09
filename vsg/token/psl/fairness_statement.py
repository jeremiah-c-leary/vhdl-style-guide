# -*- coding: utf-8 -*-

from vsg import parser


class strong_keyword(parser.keyword):
    """
    unique_id = psl_fairness_directive : strong_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class fairness_keyword(parser.keyword):
    """
    unique_id = psl_fairness_directive : fairness_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_fairness_directive : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = psl_fairness_directive : semicolon
    """

    def __init__(self, sString):
        super().__init__()
