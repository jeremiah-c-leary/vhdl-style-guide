# -*- coding: utf-8 -*-

from vsg import parser


class comma(parser.comma):
    """
    unique_id = group_constituent_list : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class group_constituent(parser.item):
    """
    unique_id = group_constituent_list : group_constituent
    """

    def __init__(self, sString):
        super().__init__(sString)
