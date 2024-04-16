# -*- coding: utf-8 -*-

from vsg import parser


class miscellaneous_operator(parser.keyword):
    """
    unique_id = miscellaneous_operator : miscellaneous_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class double_star(miscellaneous_operator):
    """
    unique_id = miscellaneous_operator : double_star
    """

    def __init__(self, sString="**"):
        super().__init__("**")


class abs_operator(miscellaneous_operator):
    """
    unique_id = miscellaneous_operator : abs_operator
    """

    def __init__(self, sString):
        super().__init__(sString)


class not_operator(miscellaneous_operator):
    """
    unique_id = miscellaneous_operator : not_operator
    """

    def __init__(self, sString):
        super().__init__(sString)
