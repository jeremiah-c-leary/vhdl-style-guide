# -*- coding: utf-8 -*-

from vsg import parser


class process_label(parser.label):
    """
    unique_id = process_statement : process_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class label_colon(parser.label_colon):
    """
    unique_id = process_statement : label_colon
    """

    def __init__(self):
        super().__init__()


class postponed_keyword(parser.keyword):
    """
    unique_id = process_statement : postponed_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class process_keyword(parser.keyword):
    """
    unique_id = process_statement : process_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = process_statement : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = process_statement : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class is_keyword(parser.keyword):
    """
    unique_id = process_statement : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class begin_keyword(parser.keyword):
    """
    unique_id = process_statement : begin_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = process_statement : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_postponed_keyword(parser.keyword):
    """
    unique_id = process_statement : end_postponed_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_process_keyword(parser.keyword):
    """
    unique_id = process_statement : end_process_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_process_label(parser.label):
    """
    unique_id = process_statement : end_process_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = process_statement : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
