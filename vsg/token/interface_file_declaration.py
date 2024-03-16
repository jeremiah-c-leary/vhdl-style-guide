# -*- coding: utf-8 -*-

from vsg import parser


class file_keyword(parser.keyword):
    """
    unique_id = interface_file_declaration : file_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class identifier(parser.identifier):
    """
    unique_id = interface_file_declaration : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class colon(parser.colon):
    """
    unique_id = interface_file_declaration : colon
    """

    def __init__(self, sString=":"):
        super().__init__()
