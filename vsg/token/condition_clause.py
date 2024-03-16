# -*- coding: utf-8 -*-

from vsg import parser


class until_keyword(parser.keyword):
    """
    unique_id = condition_clause : until_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
