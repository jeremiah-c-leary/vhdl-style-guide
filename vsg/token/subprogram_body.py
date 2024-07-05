# -*- coding: utf-8 -*-
from vsg import parser


class is_keyword(parser.keyword):
    """
    unique_id = subprogram_body : is_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class begin_keyword(parser.keyword):
    """
    unique_id = subprogram_body : begin_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = subprogram_body : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class designator(parser.designator):
    """
    unique_id = subprogram_body : designator
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = subprogram_body : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
