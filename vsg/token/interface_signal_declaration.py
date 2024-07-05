# -*- coding: utf-8 -*-

from vsg import parser


class signal_keyword(parser.keyword):
    """
    unique_id = interface_signal_declaration : signal_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = interface_signal_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = interface_signal_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class bus_keyword(parser.keyword):
    """
    unique_id = interface_signal_declaration : bus_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class assignment(parser.assignment):
    """
    unique_id = interface_signal_declaration : assignment
    """

    def __init__(self, sString):
        super().__init__(sString)
