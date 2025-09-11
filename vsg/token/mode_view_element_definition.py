# -*- coding: utf-8 -*-
from vsg import parser


class colon(parser.colon):
    """
    unique_id = mode_view_element_definition : colon
    """

    def __init__(self, sString=":"):
        super().__init__()


class semicolon(parser.semicolon):
    """
    unique_id = mode_view_element_definition : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
