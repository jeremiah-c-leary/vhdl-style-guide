# -*- coding: utf-8 -*-

from vsg import parser


class alias_keyword(parser.keyword):
    """
    unique_id = alias_declaration : alias_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class alias_designator(parser.designator):
    """
    unique_id = alias_declaration : alias_designator
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = alias_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class is_keyword(parser.keyword):
    """
    unique_id = alias_declaration : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = alias_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
