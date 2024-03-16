# -*- coding: utf-8 -*-

from vsg import parser


class keyword(parser.keyword):
    """
    unique_id = use_clause : keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class library_name(parser.name):
    """
    unique_id = use_clause : library_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class package_name(parser.name):
    """
    unique_id = use_clause : package_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class item_name(parser.name):
    """
    unique_id = use_clause : item_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class comma(parser.comma):
    """
    unique_id = use_clause : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class dot(parser.dot):
    """
    unique_id = use_clause : dot
    """

    def __init__(self, sString="."):
        super().__init__()


class all_keyword(parser.keyword):
    """
    unique_id = use_clause : all_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = use_clause : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
