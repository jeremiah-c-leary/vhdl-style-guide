# -*- coding: utf-8 -*-
from vsg import parser


class view_keyword(parser.keyword):
    """
    unique_id = element_array_mode_view_indication : view_keyword
    """

    def __init__(self, sString="view"):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = element_array_mode_view_indication : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class name(parser.name):
    """
    unique_id = element_array_mode_view_indication : name
    """

    def __init__(self, sString):
        super().__init__(sString)


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = element_array_mode_view_indication : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()
