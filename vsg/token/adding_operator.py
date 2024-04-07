# -*- coding: utf-8 -*-

from vsg import parser


class operator(parser.keyword):
    """
    unique_id = adding_operator : operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class plus(operator):
    """
    unique_id = adding_operator : plus
    """

    def __init__(self, sString="+"):
        super().__init__("+")


class minus(operator):
    """
    unique_id = adding_operator : minus
    """

    def __init__(self, sString="-"):
        super().__init__("-")


class concat(operator):
    """
    unique_id = adding_operator : concat
    """

    def __init__(self, sString="&"):
        super().__init__("&")
