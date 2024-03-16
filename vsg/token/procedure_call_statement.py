# -*- coding: utf-8 -*-

from vsg import parser


class label(parser.label):
    """
    unique_id = procedure_call_statement : label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = procedure_call_statement : label_colon
    """

    def __init__(self):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = procedure_call_statement : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
