# -*- coding: utf-8 -*-

from vsg import parser


class semicolon(parser.semicolon):
    """
    unique_id = subprogram_declaration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
