# -*- coding: utf-8 -*-

from vsg import parser


class package_keyword(parser.keyword):
    """
    unique_id = package_declaration : package_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = package_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = package_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = package_declaration : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_package_keyword(parser.keyword):
    """
    unique_id = package_declaration : end_package_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_package_simple_name(parser.simple_name):
    """
    unique_id = package_declaration : end_package_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = package_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
