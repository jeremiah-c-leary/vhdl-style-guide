# -*- coding: utf-8 -*-
from vsg import parser


class range_keyword(parser.keyword):
    """
    unique_id = index_subtype_definition : range_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class undefined_range(parser.undefined_range):
    """
    unique_id = index_subtype_definition : undefined_range
    """

    def __init__(self, sString="<>"):
        super().__init__()
