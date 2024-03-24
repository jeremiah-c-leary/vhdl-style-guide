# -*- coding: utf-8 -*-

from vsg import parser


class with_keyword(parser.keyword):
    """
    unique_id = selected_variable_assignment : with_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class select_keyword(parser.keyword):
    """
    unique_id = selected_variable_assignment : select_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class question_mark(parser.question_mark):
    """
    unique_id = selected_variable_assignment : question_mark
    """

    def __init__(self, sString="?"):
        super().__init__()


class target(parser.target):
    """
    unique_id = selected_variable_assignment : target
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = selected_variable_assignment : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = selected_variable_assignment : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
