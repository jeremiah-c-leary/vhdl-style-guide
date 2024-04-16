# -*- coding: utf-8 -*-

from vsg import parser


class for_keyword(parser.keyword):
    """
    unique_id = block_configuration : configuration_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_keyword(parser.keyword):
    """
    unique_id = block_configuration : end_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class end_for_keyword(parser.keyword):
    """
    unique_id = block_configuration : end_for_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)


class unspecified(parser.name):
    """
    unique_id = block_configuration : unspecified
    """

    def __init__(self, sString):
        super().__init__(sString)


class semicolon(parser.semicolon):
    """
    unique_id = block_configuration : semicolon
    """

    def __init__(self, sString=";"):
        super().__init__()
