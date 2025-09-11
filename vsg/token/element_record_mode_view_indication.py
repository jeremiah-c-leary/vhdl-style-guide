# -*- coding: utf-8 -*-
from vsg import parser


class view_keyword(parser.keyword):
    """
    unique_id = element_record_mode_view_indication : view_keyword
    """

    def __init__(self, sString="view"):
        super().__init__(sString)


class name(parser.name):
    """
    unique_id = element_record_mode_view_indication : name
    """

    def __init__(self, sString):
        super().__init__(sString)
