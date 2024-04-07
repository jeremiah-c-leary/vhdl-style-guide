# -*- coding: utf-8 -*-

from vsg import parser


class block_label(parser.label):
    """
    unique_id = block_statement : block_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = block_statement : label_colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class block_keyword(parser.keyword):
    """
    unique_id = block_statement : keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class guard_open_parenthesis(parser.open_parenthesis):
    """
    unique_id = block_statement : guard_open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class guard_condition(parser.item):
    """
    unique_id = block_statement : guard_condition
    """

    def __init__(self, sString):
        super().__init__(sString)


class guard_close_parenthesis(parser.close_parenthesis):
    """
    unique_id = block_statement : guard_close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class is_keyword(parser.keyword):
    """
    unique_id = block_statement : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class begin_keyword(parser.keyword):
    """
    unique_id = block_statement : begin_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = block_statement : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_block_keyword(parser.keyword):
    """
    unique_id = block_statement : end_block_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_block_label(parser.label):
    """
    unique_id = block_statement : end_block_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = block_statement : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
