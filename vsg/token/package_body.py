# -*- coding: utf-8 -*-

from vsg import parser


class package_keyword(parser.keyword):
    """
    unique_id = package_body : package_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class body_keyword(parser.keyword):
    """
    unique_id = package_body : body_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class package_simple_name(parser.simple_name):
    """
    unique_id = package_body : package_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = package_body : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = package_body : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_package_keyword(parser.keyword):
    """
    unique_id = package_body : end_package_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_body_keyword(parser.keyword):
    """
    unique_id = package_body : end_body_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_package_simple_name(parser.simple_name):
    """
    unique_id = package_body : end_package_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = package_body : semicolon
    """

    def __init__(self, sString):
        super().__init__()
