# -*- coding: utf-8 -*-

from vsg import parser


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = index_constraint : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class comma(parser.comma):
    """
    unique_id = index_constraint : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = index_constraint : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()
