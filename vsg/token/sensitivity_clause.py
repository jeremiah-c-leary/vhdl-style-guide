# -*- coding: utf-8 -*-

from vsg import parser


class on_keyword(parser.keyword):
    """
    unique_id = sensitivity_clause : on_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
