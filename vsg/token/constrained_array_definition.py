# -*- coding: utf-8 -*-

from vsg import parser


class array_keyword(parser.keyword):
    """
    unique_id = constrained_array_definition : array_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class of_keyword(parser.keyword):
    """
    unique_id = constrained_array_definition : of_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
