# -*- coding: utf-8 -*-

from vsg import parser


class begin_keyword(parser.keyword):
    """
    unique_id = generate_statement_body : begin_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = generate_statement_body : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class alternative_label(parser.label):
    """
    unique_id = generate_statement_body : alternative_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = generate_statement_body : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
