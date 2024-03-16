# -*- coding: utf-8 -*-

from vsg import parser


class while_keyword(parser.keyword):
    """
    unique_id = iteration_scheme : while_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class for_keyword(parser.keyword):
    """
    unique_id = iteration_scheme : for_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
