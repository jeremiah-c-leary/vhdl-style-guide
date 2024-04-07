# -*- coding: utf-8 -*-

from vsg import parser


class identifier(parser.identifier):
    """
    unique_id = identifier : identifier
    """

    def __init__(self, sString):
        super().__init__(sString)
