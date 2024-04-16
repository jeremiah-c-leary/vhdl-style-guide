# -*- coding: utf-8 -*-

from vsg import parser


class when_keyword(parser.keyword):
    """
    unique_id = selected_expressions : when_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class comma(parser.comma):
    """
    unique_id = selected_expressions : comma
    """

    def __init__(self, sString=","):
        super().__init__(sString)
