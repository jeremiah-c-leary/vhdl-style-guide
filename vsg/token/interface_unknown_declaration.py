# -*- coding: utf-8 -*-

from vsg import parser


class identifier(parser.identifier):
    """
    unique_id = interface_unknown_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = interface_unknown_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class bus_keyword(parser.keyword):
    """
    unique_id = interface_unknown_declaration : bus_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = interface_unknown_declaration : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)
