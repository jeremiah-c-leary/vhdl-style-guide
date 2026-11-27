# -*- coding: utf-8 -*-

from vsg import parser


class type_keyword(parser.keyword):
    """
    unique_id = interface_incomplete_type_declaration : type_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = interface_incomplete_type_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = interface_incomplete_type_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = interface_incomplete_type_declaration : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class undefined_range(parser.undefined_range):
    """
    unique_id = interface_incomplete_type_declaration : undefined_range
    """

    def __init__(self, sString="<>"):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = interface_incomplete_type_declaration : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()
