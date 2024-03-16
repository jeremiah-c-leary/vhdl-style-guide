# -*- coding: utf-8 -*-

from vsg import parser


class comma(parser.comma):
    """
    unique_id = identifier_list : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class identifier(parser.identifier):
    """
    unique_id = identifier_list : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)
