# -*- coding: utf-8 -*-

from vsg import parser


class name(parser.name):
    """
    unique_id = todo : name
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = todo : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = todo : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()
