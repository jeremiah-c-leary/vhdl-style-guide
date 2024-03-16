# -*- coding: utf-8 -*-

from vsg import parser


class access_keyword(parser.keyword):
    """
    unique_id = access_type_definition : access_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
