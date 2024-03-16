# -*- coding: utf-8 -*-

from vsg import parser


class array_keyword(parser.keyword):
    """
    unique_id = unbounded_array_definition : array_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = unbounded_array_definition : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class comma(parser.comma):
    """
    unique_id = unbounded_array_definition : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = unbounded_array_definition : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class of_keyword(parser.keyword):
    """
    unique_id = unbounded_array_definition : of_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
