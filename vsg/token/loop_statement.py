# -*- coding: utf-8 -*-

from vsg import parser


class loop_label(parser.label):
    """
    unique_id = loop_statement : loop_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = loop_statement : label_colon
    """

    def __init__(self):
        super().__init__()


class loop_keyword(parser.keyword):
    """
    unique_id = loop_statement : loop_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = loop_statement : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_loop_keyword(parser.keyword):
    """
    unique_id = loop_statement : end_loop_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_loop_label(parser.label):
    """
    unique_id = loop_statement : end_loop_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = loop_statement : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
