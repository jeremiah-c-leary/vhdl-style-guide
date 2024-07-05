# -*- coding: utf-8 -*-

from vsg import parser


class resolution_function_name(parser.name):
    """
    unique_id = resolution_indication : resolution_function_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = resolution_indication : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = resolution_indication : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()
