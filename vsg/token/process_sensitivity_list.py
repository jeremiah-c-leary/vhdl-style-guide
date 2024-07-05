# -*- coding: utf-8 -*-

from vsg import parser


class all_keyword(parser.keyword):
    """
    unique_id = process_sensitivity_list : all_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
