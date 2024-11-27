# -*- coding: utf-8 -*-
from vsg import parser


class name(parser.name):
    """
    unique_id = type_mark : name
    """

    def __init__(self, sString):
        super().__init__(sString)
