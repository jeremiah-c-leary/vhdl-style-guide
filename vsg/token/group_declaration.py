# -*- coding: utf-8 -*-

from vsg import parser


class group_keyword(parser.keyword):
    """
    unique_id = group_declaration : group_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = group_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = group_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class group_template_name(parser.name):
    """
    unique_id = group_declaration : group_template_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = group_specification : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = group_specification : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = group_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
