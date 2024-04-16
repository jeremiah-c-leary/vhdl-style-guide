# -*- coding: utf-8 -*-

from vsg import parser


class open_keyword(parser.keyword):
    """
    unique_id = file_open_information : open_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class file_open_kind_expression(parser.expression):
    """
    unique_id = file_open_information : file_open_kind_expression
    """

    def __init__(self, sString):
        super().__init__(sString)


class is_keyword(parser.keyword):
    """
    unique_id = file_open_information : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
