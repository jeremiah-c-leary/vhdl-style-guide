# -*- coding: utf-8 -*-

from vsg import parser


class label(parser.label):
    """
    unique_id = variable_assignment_statement : label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.colon):
    """
    unique_id = variable_assignment_statement : label_colon
    """

    def __init__(self, sString=";"):
        super().__init__(sString)
