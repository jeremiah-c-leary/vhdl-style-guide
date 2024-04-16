# -*- coding: utf-8 -*-
from vsg import parser


class procedure_keyword(parser.keyword):
    """
    unique_id = subprogram_kind : procedure_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class function_keyword(parser.keyword):
    """
    unique_id = subprogram_kind : function_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
