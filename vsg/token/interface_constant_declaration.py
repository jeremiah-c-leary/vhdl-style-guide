# -*- coding: utf-8 -*-

from vsg import parser


class constant_keyword(parser.keyword):
    """
    unique_id = interface_constant_declaration : constant_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = interface_constant_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = interface_constant_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class assignment(parser.assignment):
    """
    unique_id = interface_constant_declaration : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)
