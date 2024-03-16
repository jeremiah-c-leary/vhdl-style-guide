# -*- coding: utf-8 -*-

from vsg import parser


class generate_statement_label(parser.label):
    """
    unique_id = block_specification : generate_statement_label
    """

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    """
    unique_id = block_specification : open_parenthesis
    """

    def __init__(self, sString="("):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    """
    unique_id = block_specification : close_parenthesis
    """

    def __init__(self, sString=")"):
        super().__init__()


class architecture_name(parser.name):
    """
    unique_id = block_specification : architecture_name
    """

    def __init__(self, sString):
        super().__init__(sString)
