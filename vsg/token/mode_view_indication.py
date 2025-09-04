# -*- coding: utf-8 -*-

from vsg import parser


class view_keyword(parser.keyword):
    """
    unique_id = mode_view_indication : view_keyword
    """

    def __init__(self, sString="view"):
        super().__init__(sString)
