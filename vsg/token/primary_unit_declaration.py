# -*- coding: utf-8 -*-

from vsg import parser


class identifier(parser.identifier):
    """
    unique_id = primary_unit_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = primary_unit_declaration : semicolon
    """

    def __init__(self):
        super().__init__()
