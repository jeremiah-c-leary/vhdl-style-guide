# -*- coding: utf-8 -*-

from vsg import parser


class label_name(parser.label):
    """
    unique_id = psl_directive : label_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.colon):
    """
    unique_id = psl_directive : label_colon
    """

    def __init__(self, sString=":"):
        super().__init__(sString)
