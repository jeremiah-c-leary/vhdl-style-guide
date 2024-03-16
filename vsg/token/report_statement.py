# -*- coding: utf-8 -*-

from vsg import parser


class label(parser.label):
    """
    unique_id = report_statement : label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = report_statement : label_colon
    """

    def __init__(self):
        super().__init__()


class report_keyword(parser.keyword):
    """
    unique_id = report_statement : report_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class severity_keyword(parser.keyword):
    """
    unique_id = report_statement : severity_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = report_statement : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
