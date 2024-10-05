# -*- coding: utf-8 -*-

from vsg import parser


class integer(parser.integer):
    """
    unique_id = bit_string_literal : integer
    """

    def __init__(self, sString):
        super().__init__(sString)


class base_specifier(parser.item):
    """
    unique_id = bit_string_literal : base_specifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class bit_value_string(parser.item):
    """
    unique_id = bit_string_literal : bit_value_string
    """

    def __init__(self, sString):
        super().__init__(sString)
