# -*- coding: utf-8 -*-

from vsg import parser


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
