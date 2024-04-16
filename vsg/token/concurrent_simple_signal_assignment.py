# -*- coding: utf-8 -*-

from vsg import parser


class target(parser.target):
    """
    unique_id = concurrent_simple_signal_assignment : target
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = concurrent_simple_signal_assignment : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)


class guarded_keyword(parser.keyword):
    """
    unique_id = concurrent_simple_signal_assignment : guarded_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = concurrent_simple_signal_assignment : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
