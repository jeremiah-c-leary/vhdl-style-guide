# -*- coding: utf-8 -*-

from vsg import parser


class sequence_keyword(parser.keyword):
    """
    unique_id = psl_sequence_declaration : sequence_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class todo(parser.todo):
    """
    unique_id = psl_sequence_declaration : todo
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = psl_sequence_declaration : semicolon
    """

    def __init__(self, sString):
        super().__init__()
