# -*- coding: utf-8 -*-
from vsg import parser


class view_keyword(parser.keyword):
    """
    unique_id = mode_view_declaration : view_keyword
    """

    def __init__(self, sString="view"):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = mode_view_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class of_keyword(parser.keyword):
    """
    unique_id = mode_view_declaration : of_keyword
    """

    def __init__(self, sString="of"):
        super().__init__(sString)


class subtype_indication(parser.subtype_indication):
    """
    unique_id = mode_view_declaration : subtype_indication
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = mode_view_declaration : is_keyword
    """

    def __init__(self, sString="is"):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = mode_view_declaration : end_keyword
    """

    def __init__(self, sString="end"):
        super().__init__(sString)


class end_view_keyword(parser.keyword):
    """
    unique_id = mode_view_declaration : end_view_keyword
    """

    def __init__(self, sString="view"):
        super().__init__(sString)


class end_view_label(parser.label):
    """
    unique_id = mode_view_declaration : end_view_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = mode_view_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
