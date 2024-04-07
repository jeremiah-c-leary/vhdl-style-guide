# -*- coding: utf-8 -*-

from vsg import parser


class sign(parser.keyword):
    """
    unique_id = sign : sign
    """

    def __init__(self, sString):
        super().__init__(sString)


class plus(sign):
    """
    unique_id = sign : plus
    """

    def __init__(self, sString="+"):
        super().__init__("+")


class minus(sign):
    """
    unique_id = sign : minus
    """

    def __init__(self, sString="-"):
        super().__init__("-")
