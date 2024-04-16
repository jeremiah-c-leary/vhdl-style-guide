# -*- coding: utf-8 -*-

from vsg import parser


class context_keyword(parser.keyword):
    """
    unique_id = context_declaration : context_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = context_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = context_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = context_declaration : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_context_keyword(parser.keyword):
    """
    unique_id = context_declaration : end_context_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class context_simple_name(parser.simple_name):
    """
    unique_id = context_declaration : context_simple_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = context_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
