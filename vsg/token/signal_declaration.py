# -*- coding: utf-8 -*-

from vsg import parser


class signal_keyword(parser.keyword):
    """
    unique_id = signal_declaration : signal_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = signal_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = signal_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class assignment_operator(parser.assignment):
    """
    unique_id = signal_declaration : assignment_operator
    """

    def __init__(self, sString=":="):
        super().__init__(":=")


class semicolon(parser.semicolon):
    """
    unique_id = signal_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
