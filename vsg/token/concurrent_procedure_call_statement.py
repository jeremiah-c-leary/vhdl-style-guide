# -*- coding: utf-8 -*-

from vsg import parser


class label_name(parser.label):
    """
    unique_id = concurrent_procedure_call_statement : label_name
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = concurrent_procedure_call_statement : label_colon
    """

    def __init__(self):
        super().__init__()


class postponed_keyword(parser.keyword):
    """
    unique_id = concurrent_procedure_call_statement : postponed_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = concurrent_procedure_call_statement : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
