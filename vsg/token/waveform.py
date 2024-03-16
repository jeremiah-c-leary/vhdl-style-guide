# -*- coding: utf-8 -*-

from vsg import parser


class comma(parser.comma):
    """
    unique_id = waveform : comma
    """

    def __init__(self, sString=","):
        super().__init__()


class unaffected_keyword(parser.keyword):
    """
    unique_id = waveform : unaffected_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
