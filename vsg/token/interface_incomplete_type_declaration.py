# -*- coding: utf-8 -*-

from vsg import parser


class type_keyword(parser.keyword):
    """
    unique_id = interface_incomplete_type_declaration : type_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
