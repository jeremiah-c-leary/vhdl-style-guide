# -*- coding: utf-8 -*-
from vsg import parser


class if_label(parser.label):
    """
    unique_id = if_statement : if_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = if_statement : label_colon
    """

    def __init__(self):
        super().__init__()


class if_keyword(parser.keyword):
    """
    unique_id = if_statement : if_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class then_keyword(parser.keyword):
    """
    unique_id = if_statement : then_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class elsif_keyword(parser.keyword):
    """
    unique_id = if_statement : elsif_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class else_keyword(parser.keyword):
    """
    unique_id = if_statement : else_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = if_statement : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_if_keyword(parser.keyword):
    """
    unique_id = if_statement : end_if_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_if_label(parser.label):
    """
    unique_id = if_statement : end_if_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = if_statement : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
