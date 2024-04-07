# -*- coding: utf-8 -*-

from vsg import parser


class beginning(parser.comment):
    """
    unique_id = delimited_comment : beginning
    """

    def __init__(self, sString="/*"):
        super().__init__(sString)


class ending(parser.comment):
    """
    unique_id = delimited_comment : ending
    """

    def __init__(self, sString="*/"):
        super().__init__(sString)


class text(parser.item):
    """
    unique_id = delimited_comment : text
    """

    def __init__(self, sString):
        super().__init__(sString)
