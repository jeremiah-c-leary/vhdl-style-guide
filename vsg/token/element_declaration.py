# -*- coding: utf-8 -*-

from vsg import parser


class colon(parser.colon):
    """
    unique_id = element_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = element_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
