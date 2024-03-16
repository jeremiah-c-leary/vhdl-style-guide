# -*- coding: utf-8 -*-

from vsg import parser


class after_keyword(parser.keyword):
    """
    unique_id = waveform_element : after_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class null_keyword(parser.keyword):
    """
    unique_id = waveform_element : null_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
