# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import mode_view_indication


class view_keyword(mode_view_indication.view_keyword):
    """
    unique_id = array_mode_view_indication : view_keyword
    """

    def __init__(self, sString="view"):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = array_mode_view_indication : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class name(parser.name):
    """
    unique_id = array_mode_view_indication : name
    """

    def __init__(self, sString):
        super().__init__(sString)


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = array_mode_view_indication : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class of_keyword(parser.keyword):
    """
    unique_id = array_mode_view_indication : of_keyword
    """

    def __init__(self, sString="of"):
        super().__init__(sString)


class subtype_indication(parser.subtype_indication):
    """
    unique_id = array_mode_view_indication : subtype_indication
    """

    def __init__(self, sString):
        super().__init__(sString)
