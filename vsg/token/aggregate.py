# -*- coding: utf-8 -*-

from vsg import parser


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = aggregate : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = aggregate : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()
