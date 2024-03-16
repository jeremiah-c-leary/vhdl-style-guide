# -*- coding: utf-8 -*-

from vsg import parser


class keyword(parser.keyword):
    """
    unique_id = context_reference : keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class library_name(parser.selected_name):
    """
    unique_id = context_reference : library_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class context_name(parser.selected_name):
    """
    unique_id = context_reference : context_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class comma(parser.comma):
    """
    unique_id = context_reference : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class dot(parser.dot):
    """
    unique_id = context_reference : dot
    """

    def __init__(self, sString="."):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = context_reference : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
