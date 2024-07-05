# -*- coding: utf-8 -*-

from vsg import parser


class when_keyword(parser.keyword):
    """
    unique_id = case_statement_alternative : when_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = case_statement_alternative : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)
