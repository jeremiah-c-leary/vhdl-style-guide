# -*- coding: utf-8 -*-

from vsg import parser


class in_keyword(parser.keyword):
    """
    unique_id = force_mode : in_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class out_keyword(parser.keyword):
    """
    unique_id = force_mode : out_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
