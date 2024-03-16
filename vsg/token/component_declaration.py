# -*- coding: utf-8 -*-

from vsg import parser


class component_keyword(parser.keyword):
    """
    unique_id = component_declaration : component_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = component_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = component_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = component_declaration : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_component_keyword(parser.keyword):
    """
    unique_id = component_declaration : end_component_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class component_simple_name(parser.simple_name):
    """
    unique_id = component_declaration : component_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = component_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
