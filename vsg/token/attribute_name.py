# -*- coding: utf-8 -*-
from vsg import parser


class name(parser.name):
    """
    unique_id = attribute_name : name
    """

    def __init__(self, sString):
        super().__init__(sString)


class tic(parser.tic):
    """
    unique_id = attribute_name : tic
    """

    def __init__(self, sString):
        super().__init__(sString)


class attribute(parser.attribute):
    """
    unique_id = attribute_name : attribute
    """

    def __init__(self, sString):
        super().__init__(sString)
