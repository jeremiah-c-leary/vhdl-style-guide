# -*- coding: utf-8 -*-

from vsg import parser


class entity_class(parser.keyword):
    """
    unique_id = entity_specification : entity_class
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = entity_specification : colon
    """

    def __init__(self, sString=":"):
        super().__init__()
