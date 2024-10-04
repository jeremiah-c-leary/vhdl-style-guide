# -*- coding: utf-8 -*-

from vsg import parser

# TODO Maybe this gets absorbed into base_specifier?
class integer(parser.integer):
    """
    unique_id = bit_string_literal : integer
    """

    def __init__(self, sString="("):
        super().__init__()


class base_specifier(parser.item):
    """
    unique_id = bit_string_literal : base_specifier
    """

    def __init__(self, sString):
        super().__init__(sString)

# TODO Maybe this gets absorbed into bit value?
class opening_double_quote(parser.item):
    """
    unique_id = bit_string_literal : opening_double_quote
    """

    def __init__(self, sString):
        super().__init__(sString)

class bit_value(parser.item):
    """
    unique_id = bit_string_literal : bit_value
    """

    def __init__(self, sString):
        super().__init__(sString)

# TODO Maybe this gets absorbed into bit value?
class closing_double_quote(parser.item):
    """
    unique_id = bit_string_literal : closing_double_quote
    """

    def __init__(self, sString):
        super().__init__(sString)

