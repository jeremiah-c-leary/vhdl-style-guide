# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import mode_view_indication


class view_keyword(mode_view_indication.view_keyword):
    """
    unique_id = record_mode_view_indication : view_keyword
    """

    def __init__(self, sString="view"):
        super().__init__(sString)


class name(parser.name):
    """
    unique_id = record_mode_view_indication : name
    """

    def __init__(self, sString):
        super().__init__(sString)


class of_keyword(parser.keyword):
    """
    unique_id = record_mode_view_indication : of_keyword
    """

    def __init__(self, sString="of"):
        super().__init__(sString)


class subtype_indication(parser.subtype_indication):
    """
    unique_id = record_mode_view_indication : subtype_indication
    """

    def __init__(self, sString):
        super().__init__(sString)
