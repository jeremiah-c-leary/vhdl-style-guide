# -*- coding: utf-8 -*-

from vsg import parser


class identifier(parser.identifier):
    """
    unique_id = parameter_specification : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)


class in_keyword(parser.keyword):
    """
    unique_id = parameter_specification : in_keyword
    """

    def __init__(self, sString):
        super().__init__(sString)
