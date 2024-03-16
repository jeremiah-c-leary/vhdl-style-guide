# -*- coding: utf-8 -*-

from vsg import parser


class package_keyword(parser.keyword):
    """
    unique_id = package_instantiation_declaration : package_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = package_instantiation_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class new_keyword(parser.keyword):
    """
    unique_id = package_instantiation_declaration : new_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class uninstantiated_package_name(parser.name):
    """
    unique_id = package_instantiation_declaration : uninstantiated_package_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = package_instantiation_declaration : semicolon
    """

    def __init__(self, sString):
        super().__init__()
