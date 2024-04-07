# -*- coding: utf-8 -*-

from vsg import parser


class with_keyword(parser.keyword):
    """
    unique_id = concurrent_selected_signal_assignment : with_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class select_keyword(parser.keyword):
    """
    unique_id = concurrent_selected_signal_assignment : select_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class target(parser.target):
    """
    unique_id = concurrent_selected_signal_assignment : target
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = concurrent_selected_signal_assignment : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)


class guarded_keyword(parser.keyword):
    """
    unique_id = concurrent_selected_signal_assignment : guarded_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = concurrent_selected_signal_assignment : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()


class question_mark(parser.question_mark):
    """
    unique_id = concurrent_selected_signal_assignment : question_mark
    """

    def __init__(self, sString="?"):
        super().__init__()
