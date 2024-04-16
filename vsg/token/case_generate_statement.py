# -*- coding: utf-8 -*-

from vsg import parser


class generate_label(parser.label):
    """
    unique_id = case_generate_statement : generate_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = case_generate_statement : label_colon
    """

    def __init__(self):
        super().__init__()


class case_keyword(parser.keyword):
    """
    unique_id = case_generate_statement : case_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class generate_keyword(parser.keyword):
    """
    unique_id = case_generate_statement : generate_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = case_generate_statement : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_generate_keyword(parser.keyword):
    """
    unique_id = case_generate_statement : end_generate_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_generate_label(parser.label):
    """
    unique_id = case_generate_statement : end_generate_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = case_generate_statement : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
