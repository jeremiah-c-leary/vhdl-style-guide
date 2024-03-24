# -*- coding: utf-8 -*-

from vsg import parser


class target(parser.target):
    """
    unique_id = conditional_force_assignment : target
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = conditional_force_assignment : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)


class force_keyword(parser.keyword):
    """
    unique_id = conditional_force_assignment : force_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = conditional_force_assignment : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
