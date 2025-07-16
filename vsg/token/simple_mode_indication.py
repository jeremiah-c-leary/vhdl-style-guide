# -*- coding: utf-8 -*-

from vsg import parser


class subtype_indication(parser.subtype_indication):
    """
    unique_id = subtype_indication : subtype_indication
    """

    def __init__(self, sString):
        super().__init__(sString)


class bus_keyword(parser.keyword):
    """
    unique_id = simple_mode_indication : bus_keyword
    """

    def __init__(self, sString="bus"):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = simple_mode_indication : assignment
    """

    def __init__(self, sString=":="):
        super().__init__(sString)


class expression(parser.expression):
    """
    unique_id = simple_mode_indication : expression
    """

    def __init__(self, sString):
        super().__init__(sString)
