# -*- coding: utf-8 -*-

from vsg import parser


class file_keyword(parser.keyword):
    """
    unique_id = file_type_definition : file_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class of_keyword(parser.keyword):
    """
    unique_id = file_type_definition : of_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
