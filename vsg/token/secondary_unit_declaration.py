# -*- coding: utf-8 -*-

from vsg import parser


class identifier(parser.identifier):
    """
    unique_id = secondary_unit_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class equal_sign(parser.item):
    """
    unique_id = secondary_unit_declaration : equal_sign
    """

    def __init__(self):
        super().__init__("=")


class physical_literal(parser.item):
    """
    unique_id = secondary_unit_declaration : physical_literal
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = secondary_unit_declaration : semicolon
    """

    def __init__(self):
        super().__init__()
